from PySide6.QtWidgets import QGridLayout, QDialog, QDialogButtonBox, QLabel, QLineEdit, QMessageBox, QWidget
from PySide6.QtGui import QIcon, QCloseEvent
from PySide6.QtCore import Signal, Qt

from CAMELS.utility import device_handling, variables_handling

from pkg_resources import resource_filename


class Manual_Control(QWidget):
    closing = Signal()

    def __init__(self, parent=None, title='Manual Control', control_data=None):
        super().__init__()
        # layout = QGridLayout()
        # self.setLayout(layout)
        control_data = control_data or {}

        self.setWindowTitle(f'CAMELS - {title}')
        self.setWindowIcon(QIcon(resource_filename('CAMELS', 'graphics/camels_icon.png')))
        self.name = title
        self.device = None
        self.ophyd_device = None
        self.device_list = []
        self.show()

    # def close(self) -> bool:
    #     # device_handling.close_devices(self.device_list)
    #     self.closing.emit()
    #     return super().close()

    def closeEvent(self, a0: QCloseEvent) -> None:
        device_handling.close_devices(self.device_list)
        self.closing.emit()
        return super().closeEvent(a0)

    def start_device(self, device_name):
        self.device = variables_handling.devices[device_name]
        if self.device:
            self.device_list = self.device.get_necessary_devices()
            self.device_list = list(set(self.device_list))
            if self.device.name in self.device_list:
                self.device_list.remove(self.device.custom_name)
            self.device_list.append(self.device.custom_name)
            devs, dev_data = device_handling.instantiate_devices(self.device_list)
            self.ophyd_device = devs[self.device.custom_name]



class Manual_Control_Config(QDialog):
    def __init__(self, parent=None, control_data=None, title='Manual Control Config', control_type=''):
        super().__init__(parent=parent)
        self.setWindowFlags(self.windowFlags() | Qt.WindowMaximizeButtonHint)
        layout = QGridLayout()
        self.setLayout(layout)
        self.control_type = control_type or 'Manual_Control'

        self.setWindowTitle(f'{title} - CAMELS')

        self.buttonBox = QDialogButtonBox()
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.accepted.connect(self.accept)

        name_label = QLabel('Name:')
        self.control_data = control_data or {}
        if 'name' in self.control_data:
            name = self.control_data['name']
        else:
            name = self.control_type
        self.lineEdit_name = QLineEdit(name)

        layout.addWidget(name_label, 0, 0)
        layout.addWidget(self.lineEdit_name, 0, 1)
        layout.addWidget(self.buttonBox, 11, 0, 1, 2)

    def accept(self):
        self.control_data['name'] = self.lineEdit_name.text()
        self.control_data['control_type'] = self.control_type
        super().accept()

    def closeEvent(self, a0: QCloseEvent) -> None:
        discard_dialog = QMessageBox.question(self, 'Discard Changes?',
                                              f'All changes will be lost!',
                                              QMessageBox.Yes | QMessageBox.No)
        if discard_dialog != QMessageBox.Yes:
            a0.ignore()
            return
        super().closeEvent(a0)

