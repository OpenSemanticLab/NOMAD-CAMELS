# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow_v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(736, 490)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_arrow = QtWidgets.QLabel(self.centralwidget)
        self.label_arrow.setText("")
        self.label_arrow.setAlignment(QtCore.Qt.AlignCenter)
        self.label_arrow.setObjectName("label_arrow")
        self.gridLayout_5.addWidget(self.label_arrow, 2, 2, 1, 1)
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setEnabled(False)
        self.pushButton_stop.setMaximumSize(QtCore.QSize(130, 16777215))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.gridLayout_5.addWidget(self.pushButton_stop, 4, 11, 1, 1)
        self.pushButton_resume = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_resume.setEnabled(False)
        self.pushButton_resume.setMaximumSize(QtCore.QSize(130, 16777215))
        self.pushButton_resume.setObjectName("pushButton_resume")
        self.gridLayout_5.addWidget(self.pushButton_resume, 4, 9, 1, 1)
        self.pushButton_pause = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pause.setEnabled(False)
        self.pushButton_pause.setMaximumSize(QtCore.QSize(130, 16777215))
        self.pushButton_pause.setObjectName("pushButton_pause")
        self.gridLayout_5.addWidget(self.pushButton_pause, 4, 10, 1, 1)
        self.progressBar_protocols = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_protocols.setMaximumSize(QtCore.QSize(400, 16777215))
        self.progressBar_protocols.setProperty("value", 0)
        self.progressBar_protocols.setObjectName("progressBar_protocols")
        self.gridLayout_5.addWidget(self.progressBar_protocols, 5, 9, 1, 3)
        self.textEdit_console_output = Console_TextEdit(self.centralwidget)
        self.textEdit_console_output.setMaximumSize(QtCore.QSize(400, 16777215))
        self.textEdit_console_output.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit_console_output.setObjectName("textEdit_console_output")
        self.gridLayout_5.addWidget(self.textEdit_console_output, 6, 9, 2, 3)
        self.label_no_instruments = QtWidgets.QLabel(self.centralwidget)
        self.label_no_instruments.setObjectName("label_no_instruments")
        self.gridLayout_5.addWidget(self.label_no_instruments, 2, 3, 1, 9)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setObjectName("widget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.comboBox_user = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_user.setFont(font)
        self.comboBox_user.setObjectName("comboBox_user")
        self.gridLayout_6.addWidget(self.comboBox_user, 0, 2, 1, 1)
        self.pushButton_manage_instr = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_manage_instr.setFont(font)
        self.pushButton_manage_instr.setObjectName("pushButton_manage_instr")
        self.gridLayout_6.addWidget(self.pushButton_manage_instr, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 1, 1, 1)
        self.pushButton_editUserInfo = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_editUserInfo.setFont(font)
        self.pushButton_editUserInfo.setObjectName("pushButton_editUserInfo")
        self.gridLayout_6.addWidget(self.pushButton_editUserInfo, 0, 3, 1, 1)
        self.comboBox_sample = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_sample.setFont(font)
        self.comboBox_sample.setObjectName("comboBox_sample")
        self.gridLayout_6.addWidget(self.comboBox_sample, 0, 7, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 0, 5, 1, 1)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_6.addWidget(self.line, 0, 4, 1, 1)
        self.pushButton_editSampleInfo = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_editSampleInfo.setFont(font)
        self.pushButton_editSampleInfo.setObjectName("pushButton_editSampleInfo")
        self.gridLayout_6.addWidget(self.pushButton_editSampleInfo, 0, 8, 1, 1)
        self.gridLayout_5.addWidget(self.widget, 1, 2, 1, 10)
        self.label_logo = QtWidgets.QLabel(self.centralwidget)
        self.label_logo.setMaximumSize(QtCore.QSize(16777215, 70))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("../graphics/camels_horizontal.png"))
        self.label_logo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_logo.setObjectName("label_logo")
        self.gridLayout_5.addWidget(self.label_logo, 8, 9, 1, 3)
        self.main_splitter = QtWidgets.QSplitter(self.centralwidget)
        self.main_splitter.setOrientation(QtCore.Qt.Vertical)
        self.main_splitter.setObjectName("main_splitter")
        self.manual_widget = QtWidgets.QWidget(self.main_splitter)
        self.manual_widget.setObjectName("manual_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.manual_widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.pushButton_add_manual = QtWidgets.QPushButton(self.manual_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add_manual.sizePolicy().hasHeightForWidth())
        self.pushButton_add_manual.setSizePolicy(sizePolicy)
        self.pushButton_add_manual.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_add_manual.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(75)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_add_manual.setFont(font)
        self.pushButton_add_manual.setStyleSheet("QPushButton {\n"
"    font-family: Calibri;\n"
"    font-size: 75pt;\n"
"    font-weight: bold;\n"
"    padding: 0px;\n"
"    padding-bottom: 10px;\n"
"}")
        self.pushButton_add_manual.setObjectName("pushButton_add_manual")
        self.gridLayout.addWidget(self.pushButton_add_manual, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.manual_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
"    font-family: Calibri;\n"
"    font-size: 20pt;\n"
"    font-weight: bold;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.meas_widget = QtWidgets.QWidget(self.main_splitter)
        self.meas_widget.setObjectName("meas_widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.meas_widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.meas_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n"
"    font-family: Calibri;\n"
"    font-size: 20pt;\n"
"    font-weight: bold;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.pushButton_add_meas = QtWidgets.QPushButton(self.meas_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add_meas.sizePolicy().hasHeightForWidth())
        self.pushButton_add_meas.setSizePolicy(sizePolicy)
        self.pushButton_add_meas.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_add_meas.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(75)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton_add_meas.setFont(font)
        self.pushButton_add_meas.setStyleSheet("QPushButton {\n"
"    font-family: Calibri;\n"
"    font-size: 75pt;\n"
"    font-weight: bold;\n"
"    padding: 0px;\n"
"    padding-bottom: 10px;\n"
"}")
        self.pushButton_add_meas.setObjectName("pushButton_add_meas")
        self.gridLayout_2.addWidget(self.pushButton_add_meas, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.main_splitter, 4, 2, 5, 7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 736, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPresets = QtWidgets.QAction(MainWindow)
        self.actionPresets.setObjectName("actionPresets")
        self.actionOptions = QtWidgets.QAction(MainWindow)
        self.actionOptions.setObjectName("actionOptions")
        self.actionSave_Device_Preset_As = QtWidgets.QAction(MainWindow)
        self.actionSave_Device_Preset_As.setObjectName("actionSave_Device_Preset_As")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionMeasurement_Presets = QtWidgets.QAction(MainWindow)
        self.actionMeasurement_Presets.setObjectName("actionMeasurement_Presets")
        self.actionSave_Preset = QtWidgets.QAction(MainWindow)
        self.actionSave_Preset.setObjectName("actionSave_Preset")
        self.actionOpen_Backup_Device_Preset = QtWidgets.QAction(MainWindow)
        self.actionOpen_Backup_Device_Preset.setObjectName("actionOpen_Backup_Device_Preset")
        self.actionLoad_Backup_Preset = QtWidgets.QAction(MainWindow)
        self.actionLoad_Backup_Preset.setObjectName("actionLoad_Backup_Preset")
        self.actionAutosave_on_closing = QtWidgets.QAction(MainWindow)
        self.actionAutosave_on_closing.setCheckable(True)
        self.actionAutosave_on_closing.setObjectName("actionAutosave_on_closing")
        self.actionDevice_Driver_Builder = QtWidgets.QAction(MainWindow)
        self.actionDevice_Driver_Builder.setObjectName("actionDevice_Driver_Builder")
        self.actionDark_Mode = QtWidgets.QAction(MainWindow)
        self.actionDark_Mode.setCheckable(True)
        self.actionDark_Mode.setObjectName("actionDark_Mode")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionIOC_Builder = QtWidgets.QAction(MainWindow)
        self.actionIOC_Builder.setObjectName("actionIOC_Builder")
        self.actionNew_Device_Preset_2 = QtWidgets.QAction(MainWindow)
        self.actionNew_Device_Preset_2.setObjectName("actionNew_Device_Preset_2")
        self.actionSave_Device_Preset = QtWidgets.QAction(MainWindow)
        self.actionSave_Device_Preset.setObjectName("actionSave_Device_Preset")
        self.actionSave_Preset_As = QtWidgets.QAction(MainWindow)
        self.actionSave_Preset_As.setObjectName("actionSave_Preset_As")
        self.actionNew_Preset = QtWidgets.QAction(MainWindow)
        self.actionNew_Preset.setObjectName("actionNew_Preset")
        self.actionNew_Device_Preset = QtWidgets.QAction(MainWindow)
        self.actionNew_Device_Preset.setObjectName("actionNew_Device_Preset")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionReport_Bug = QtWidgets.QAction(MainWindow)
        self.actionReport_Bug.setObjectName("actionReport_Bug")
        self.actionVISA_device_builder = QtWidgets.QAction(MainWindow)
        self.actionVISA_device_builder.setObjectName("actionVISA_device_builder")
        self.menuFile.addAction(self.actionNew_Preset)
        self.menuFile.addAction(self.actionSave_Preset)
        self.menuFile.addAction(self.actionSave_Preset_As)
        self.menuFile.addAction(self.actionLoad_Backup_Preset)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addAction(self.actionReport_Bug)
        self.menuTools.addAction(self.actionDevice_Driver_Builder)
        self.menuTools.addAction(self.actionVISA_device_builder)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_stop.setText(_translate("MainWindow", "Stop"))
        self.pushButton_resume.setText(_translate("MainWindow", "Resume"))
        self.pushButton_pause.setText(_translate("MainWindow", "Pause"))
        self.label_no_instruments.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">You are currently using no instruments.</span></p><p><span style=\" font-size:12pt; font-weight:600;\">Click &quot;Manage Instruments&quot; to configure your</span></p><p><span style=\" font-size:12pt; font-weight:600;\">first instrument and start with CAMELS!</span></p></body></html>"))
        self.pushButton_manage_instr.setText(_translate("MainWindow", "Mangage\n"
"Instruments"))
        self.label.setText(_translate("MainWindow", "User:"))
        self.pushButton_editUserInfo.setText(_translate("MainWindow", "Edit User-Information"))
        self.label_8.setText(_translate("MainWindow", "Sample:"))
        self.pushButton_editSampleInfo.setText(_translate("MainWindow", "Edit Sample-Information"))
        self.pushButton_add_manual.setText(_translate("MainWindow", "+"))
        self.label_2.setText(_translate("MainWindow", "Manual Control"))
        self.label_3.setText(_translate("MainWindow", "Measurement Protocols"))
        self.pushButton_add_meas.setText(_translate("MainWindow", "+"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionPresets.setText(_translate("MainWindow", "Device-Presets"))
        self.actionOptions.setText(_translate("MainWindow", "Options"))
        self.actionSave_Device_Preset_As.setText(_translate("MainWindow", "Save Device Preset As"))
        self.actionLoad.setText(_translate("MainWindow", "Open"))
        self.actionMeasurement_Presets.setText(_translate("MainWindow", "Measurement-Presets"))
        self.actionSave_Preset.setText(_translate("MainWindow", "Save Preset"))
        self.actionOpen_Backup_Device_Preset.setText(_translate("MainWindow", "Load Backup Device Preset"))
        self.actionLoad_Backup_Preset.setText(_translate("MainWindow", "Load Preset"))
        self.actionAutosave_on_closing.setText(_translate("MainWindow", "Autosave on closing"))
        self.actionDevice_Driver_Builder.setText(_translate("MainWindow", "Update CAMELS"))
        self.actionDark_Mode.setText(_translate("MainWindow", "Dark Mode"))
        self.actionUndo.setText(_translate("MainWindow", "Undo (ctrl + z)"))
        self.actionRedo.setText(_translate("MainWindow", "Redo (ctrl + y)"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionIOC_Builder.setText(_translate("MainWindow", "IOC-Builder"))
        self.actionNew_Device_Preset_2.setText(_translate("MainWindow", "New Device Preset"))
        self.actionSave_Device_Preset.setText(_translate("MainWindow", "Save Device Preset"))
        self.actionSave_Preset_As.setText(_translate("MainWindow", "Save Preset As"))
        self.actionNew_Preset.setText(_translate("MainWindow", "New Preset"))
        self.actionNew_Device_Preset.setText(_translate("MainWindow", "New Device Preset"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionReport_Bug.setText(_translate("MainWindow", "Report Bug"))
        self.actionVISA_device_builder.setText(_translate("MainWindow", "VISA-device builder"))
from CAMELS.ui_widgets.console_redirect import Console_TextEdit
