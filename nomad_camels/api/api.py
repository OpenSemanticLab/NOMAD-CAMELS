import sys

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.responses import JSONResponse, FileResponse, RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from PySide6.QtCore import QThread, Signal
from nomad_camels.frontpanels.settings_window import hash_api_key
from nomad_camels.utility import load_save_functions
import uvicorn
import sqlite3
import os
import threading
import time
import json


# Define the validate_api_key function
def validate_api_key(api_key: str) -> bool:
    # Establish the SQLite connection and cursor
    data_base_path = os.path.join(
        load_save_functions.appdata_path, "CAMELS_API_keys.db"
    )
    conn = sqlite3.connect(data_base_path)
    c = conn.cursor()
    hashed_key = hash_api_key(api_key)
    # Catch exception where the api:keys table does not exist anymore
    try:
        c.execute("SELECT * FROM api_keys WHERE key = ?", (hashed_key,))
    except sqlite3.OperationalError as e:
        if "no such table: api_keys" in str(e):
            conn.close()
            return False
        else:
            raise  # Re-raise the exception if it's not the specific one we're looking for
    result = c.fetchone()
    conn.close()
    return result is not None


# Initialize HTTP Basic Authentication
security = HTTPBasic()


# Define the dependency for API key validation
async def validate_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    api_key = credentials.password
    # The api_key is directly taken from credentials.password
    if api_key and validate_api_key(api_key):
        return True
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid API Key",
        headers={"WWW-Authenticate": "Basic"},
    )


class FastapiThread(QThread):
    # Define signals for communicating with the main window
    # Signal to start a protocol
    start_protocol_signal = Signal(str)
    # Signal to send error message to main window, clears the fastapi_thread variable
    port_error_signal = Signal(str)
    # Signal to set the available user names
    set_user_signal = Signal(str)
    # Signal to set the sample in the main window
    set_sample_signal = Signal(str)
    # Signal to set the session name in the main window
    set_session_signal = Signal(str)
    # Signal to queue a protocol
    queue_protocol_signal = Signal(str)
    # Signal to remove a protocol from the queue
    remove_queue_protocol_signal = Signal(str)
    # Signal to check the checkbox of the next protocol in the queue
    set_checkbox_signal = Signal(str)

    def __init__(self, main_window, api_port):
        super().__init__()
        # get the main window so that we have access to all the settings and dictionaries
        self.main_window = main_window
        self.api_port = api_port
        self._stop_event = threading.Event()
        self.app = FastAPI()  # Initialize the FastAPI app

    def run(self):
        app = self.app
        # Define the API endpoints

        # Get the list of available protocols
        @app.get("/api/v1/protocols")
        async def get_protocols(api_key: str = Depends(validate_credentials)):
            """Get the list of available protocols"""
            return JSONResponse(
                content={"Protocols": list(self.main_window.protocols_dict.keys())}
            )

        # Run a protocol by name
        @app.get("/api/v1/actions/run/protocols/{protocol_name}")
        async def run_protocol(
            protocol_name: str, api_key: str = Depends(validate_credentials)
        ):
            """Run a protocol by name"""
            self.start_protocol_signal.emit(str(protocol_name))
            return JSONResponse(content={"status": "success"})

        # Get the current protocol queue
        @app.get("/api/v1/queue")
        async def get_queue(api_key: str = Depends(validate_credentials)):
            """Get the current protocol queue"""
            protocols = list(
                self.main_window.run_queue_widget.protocol_name_variables.values()
            )
            indexed_protocols = [
                [index] + protocol for index, protocol in enumerate(protocols)
            ]
            return JSONResponse(content=indexed_protocols)

        @app.get("/api/v1/actions/queue/protocols/{protocol_name}")
        async def queue_protocol(
            protocol_name: str, api_key: str = Depends(validate_credentials)
        ):
            """Add a protocol to the queue by name"""
            try:
                self.queue_protocol_signal.emit(str(protocol_name))
            except ValueError as e:
                raise HTTPException(
                    status_code=500,
                    detail=f"Failed to add protocol {protocol_name} to queue as the protocol was not found.\n{e}",
                )
            time.sleep(0.05)
            protocol_values = list(
                self.main_window.run_queue_widget.protocol_name_variables.values()
            )
            if len(protocol_values) > 0:
                # Get the name of the last protocol in the queue
                last_protocol = protocol_values[-1]
                last_protocol_name = last_protocol[0]
                # Check if the provided protocol name matches the last one in the queue
                if protocol_name == last_protocol_name:
                    return JSONResponse(
                        content={"status": "success adding protocol to queue"}
                    )
                else:
                    raise HTTPException(
                        status_code=500,
                        detail=f"Failed to add protocol {protocol_name} to queue as the protocol was not found.",
                    )
            else:
                # Return a failure response if the queue is empty
                raise HTTPException(
                    status_code=500,
                    detail=f"Failed to add protocol {protocol_name} to queue as the protocol was not found.",
                )

        # Remove protocol from queue
        @app.get("/api/v1/actions/queue_remove/protocols/{protocol_name}_{index}")
        async def remove_protocol(
            protocol_name: str, index: int, api_key: str = Depends(validate_credentials)
        ):
            """Remove a protocol from the queue by name"""
            # Get the current queue
            queue_response = await get_queue(api_key)
            # Extract the queue content from the JSON response
            queue_content = queue_response.body.decode("utf-8")
            queue_list = json.loads(queue_content)
            qt_items = list(
                self.main_window.run_queue_widget.protocol_name_variables.keys()
            )
            for item in queue_list:
                if item[1] == protocol_name and item[0] == index:
                    self.remove_queue_protocol_signal.emit(str(qt_items[index]))
                    return JSONResponse(
                        content={"status": "success removing protocol from queue"}
                    )
            raise HTTPException(
                status_code=500,
                detail=f"Failed to remove protocol {protocol_name} with index {index} from queue as the protocol was not found at that position.",
            )

        # Check the ready checkbox of protocols in the queue
        @app.get("/api/v1/actions/queue_check_next/protocols/{protocol_name}_{index}")
        async def check_next_protocol(
            protocol_name: str, index: int, api_key: str = Depends(validate_credentials)
        ):
            """Check the ready checkbox of protocols in the queue"""
            # Get the current queue
            queue_response = await get_queue(api_key)
            # Extract the queue content from the JSON response
            queue_content = queue_response.body.decode("utf-8")
            queue_list = json.loads(queue_content)
            qt_items = list(
                self.main_window.run_queue_widget.protocol_name_variables.keys()
            )
            for item in queue_list:
                if item[1] == protocol_name and item[0] == index:
                    self.set_checkbox_signal.emit(str(qt_items[index]))
                    return JSONResponse(
                        content={"status": "success checking next protocol"}
                    )
            raise HTTPException(
                status_code=500,
                detail=f"Failed to check next protocol {protocol_name} with index {index} from queue as the protocol was not found at that position.",
            )

        @app.get("/api/v1/samples")
        async def get_samples(api_key: str = Depends(validate_credentials)):
            """Get the list of available samples"""
            return JSONResponse(content=self.main_window.sampledata)

        @app.get("/api/v1/actions/set/samples/{sample_name}")
        async def set_samples(
            sample_name: str, api_key: str = Depends(validate_credentials)
        ):
            """Set the active sample"""
            self.set_sample_signal.emit(str(sample_name))
            time.sleep(0.01)
            if self.main_window.active_sample == sample_name:
                return JSONResponse(content={"status": "success setting sample name"})
            else:
                return JSONResponse(content={"status": "failed setting sample name"})

        @app.get("/api/v1/users")
        async def get_users(api_key: str = Depends(validate_credentials)):
            """Get the list of available users"""
            return JSONResponse(content=self.main_window.userdata)

        @app.get("/api/v1/actions/set/users/{user_name}")
        async def set_users(
            user_name: str, api_key: str = Depends(validate_credentials)
        ):
            """Set the active user"""
            self.set_user_signal.emit(str(user_name))
            time.sleep(0.01)
            if self.main_window.active_user == user_name:
                return JSONResponse(content={"status": "success setting user name"})
            else:
                return JSONResponse(content={"status": "failed setting user name"})

        @app.get("/api/v1/session")
        async def get_session(api_key: str = Depends(validate_credentials)):
            """Get the current session name"""
            return JSONResponse(content=self.main_window.lineEdit_session.text())

        @app.get("/api/v1/actions/set/session/{session_name}")
        async def set_session(
            session_name: str, api_key: str = Depends(validate_credentials)
        ):
            """Set the active session name"""
            self.set_session_signal.emit(str(session_name))
            time.sleep(0.01)
            if self.main_window.lineEdit_session.text() == session_name:
                return JSONResponse(content={"status": "success setting session name"})
            else:
                return JSONResponse(content={"status": "failed setting session name"})

        # TODO: Fix this to actually work using the body of the POST!!
        # @app.post("/protocol/{protocol_name}")
        # async def run_protocol(protocol_name: str, api_key: str = Depends(validate_credentials)):
        #     self.start_protocol_signal.emit(str(protocol_name))
        #     return JSONResponse(content={"status": "success"})

        # Root redirects to the API documentation
        @app.get("/")
        async def root():
            return RedirectResponse(url="/docs", status_code=302)

        # Define a favicon endpoint
        @app.get("/favicon.ico")
        async def favicon():
            icon_path = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "../graphics/camels_icon_high_res.ico",
            )
            return FileResponse(icon_path)

        @app.get("/logout")
        async def logout():
            """Logout the user"""
            raise HTTPException(status_code=401, detail="Successful Logout completed")

        # Start the uvicorn server
        try:
            self.server_config = uvicorn.Config(
                app, host="127.0.0.1", port=int(self.api_port), log_level="info"
            )
            self.server = uvicorn.Server(self.server_config)

            # Run the server
            self.server.run()
        except ValueError:  # Catching ValueError for invalid port conversion
            print(f"Invalid port number: {self.api_port}")
            self.port_error_signal.emit("Invalid port number")
        except Exception as e:
            print(f"Error starting server: {e}")
            self.port_error_signal.emit("Failed to start server")

    def stop_server(self):  #  Method to trigger shutdown
        if self.server is not None:
            self.server.should_exit = True
            self._stop_event.set()
            self.quit()
            self.wait()


if __name__ == "__main__":

    class fake_run_queue_widget:
        protocol_name_variables = {
            "key1": ["execute", {"factor": 3, "results": 0}],
            "key2": ["execute2", {"factor": 3, "results": 0}],
            "key3": ["execute3", {"factor": 3, "results": 0}],
        }

    # Create a fake main window for testing
    class fake_main_window:
        def __init__(self):
            self.protocols_dict = {"test_protocol": "test_protocol"}
            self.run_queue_widget = None
            self.sampledata = {"sample1": "sample1"}
            self.userdata = {"user1": "user1"}
            self.lineEdit_session = None
            self.active_sample = None
            self.active_user = None
            self.run_queue_widget = fake_run_queue_widget()

    api_thread = FastapiThread(main_window=fake_main_window(), api_port=12345)
    api_thread.start()
    api_thread.wait()  # Ensure the main thread waits for the server thread to finish
