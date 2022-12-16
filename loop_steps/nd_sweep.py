from PyQt5.QtWidgets import QComboBox, QLabel, QCheckBox
from PyQt5.QtGui import QFont

from main_classes.loop_step import Loop_Step_Config, Loop_Step
from utility import variables_handling
from utility.channels_check_table import Channels_Check_Table
from utility.load_save_helper_functions import load_plots
from bluesky_handling.builder_helper_functions import plot_creator
from frontpanels.plot_definer import Plot_Button_Overview

from loop_steps.for_while_loops import For_Loop_Step_Config_Sub, For_Loop_Step



class ND_Sweep(Loop_Step):
    def __init__(self, name='', children=None, parent_step=None, step_info=None,
                 **kwargs):
        super().__init__(name, children, parent_step, step_info, **kwargs)
        step_info = step_info or {}
        self.step_type = 'n-D Sweep'
        self.has_children = False
        self.sweep_channels = step_info['sweep_channels'] if 'sweep_channels' in step_info else []
        self.data_output = step_info['data_output'] if 'data_output' in step_info else 'sub-stream'
        self.plots = load_plots([], step_info['plots']) if 'plots' in step_info else []
        self.read_channels = step_info['read_channels'] if 'read_channels' in step_info else []
        self.use_own_plots = step_info['use_own_plots'] if 'use_own_plots' in step_info else False
        self.calc_minmax = step_info['calc_minmax'] if 'calc_minmax' in step_info else False
        self.calc_mean = step_info['calc_mean'] if 'calc_mean' in step_info else False
        self.calc_stddev = step_info['calc_stddev'] if 'calc_stddev' in step_info else False

    def update_used_devices(self):
        self.used_devices = []
        for channel in self.read_channels:
            if channel in variables_handling.channels:
                device = variables_handling.channels[channel].device
                if device not in self.used_devices:
                    self.used_devices.append(device)
        for channel in self.sweep_channels:
            if channel in variables_handling.channels:
                device = variables_handling.channels[channel].device
                if device not in self.used_devices:
                    self.used_devices.append(device)

    def get_outer_string(self):
        if self.use_own_plots:
            return plot_creator(self.plots, f'create_plots_{self.name}')[0]
        return ''

    def get_add_main_string(self):
        stream = f'"{self.name}"'
        if self.data_output == 'main stream':
            stream = '"primary"'
        add_main_string = ''
        if self.use_own_plots:
            add_main_string += f'\treturner["{self.name}_plot_stuff"] = create_plots_{self.name}(RE, {stream})\n'
        return add_main_string


class ND_Sweep_Config(Loop_Step_Config):
    def __init__(self, loop_step:ND_Sweep, parent=None):
        super().__init__(parent, loop_step)
        self.loop_step = loop_step
        label_sweep_channel = QLabel('Sweep Channel')
        out_box = []
        in_box = []
        for channel in variables_handling.channels:
            in_box.append(channel)
            if variables_handling.channels[channel].output:
                out_box.append(channel)
        self.comboBox_sweep_channel = QComboBox()
        self.comboBox_sweep_channel.addItems(out_box)
        if loop_step.sweep_channel in out_box:
            self.comboBox_sweep_channel.setCurrentText(loop_step.sweep_channel)

        label_data = QLabel('Data Output:')
        self.comboBox_data_output = QComboBox()
        output_types = ['sub-stream', 'main stream', 'own file']
        self.comboBox_data_output.addItems(output_types)
        self.comboBox_data_output.setCurrentText(loop_step.data_output)

        self.sweep_widget = For_Loop_Step_Config_Sub(parent=self,
                                                     loop_step=loop_step)

        # self.read_table = AddRemoveTable(title='Read Channels', headerLabels=[],
        #                                  tableData=loop_step.read_channels,
        #                                  comboBoxes=in_box)
        labels = ['read', 'channel']
        info_dict = {'channel': self.loop_step.read_channels}
        self.read_table = Channels_Check_Table(self, labels, info_dict=info_dict)

        self.checkBox_use_own_plots = QCheckBox('Use own Plots')
        self.checkBox_use_own_plots.setChecked(loop_step.use_own_plots)

        self.plot_widge = Plot_Button_Overview(self, self.loop_step.plots)

        label_proc = QLabel('Data processing')
        font = QFont()
        font.setBold(True)
        label_proc.setStyleSheet('font-size: 9pt')
        label_proc.setFont(font)
        self.checkBox_minmax = QCheckBox('Calculate min/max')
        self.checkBox_minmax.setChecked(loop_step.calc_minmax)
        self.checkBox_mean = QCheckBox('Calculate mean')
        self.checkBox_mean.setChecked(loop_step.calc_mean)
        self.checkBox_stddev = QCheckBox('Calculate standard deviation')
        self.checkBox_stddev.setChecked(loop_step.calc_stddev)
        # self.checkBox_fit = QCheckBox('Calculate fit')
        # self.checkBox_fit.setChecked(loop_step.calc_fit)
        # self.checkBox_fit.clicked.connect(self.change_fitting)
        # self.checkBox_guess_fit = QCheckBox('Guess initial params')
        # self.checkBox_guess_fit.setChecked(loop_step.guess_fit_params)
        # self.checkBox_guess_fit.clicked.connect(self.change_fitting)
        # self.radioButton_predev = QRadioButton('Predefined function')
        # self.radioButton_own = QRadioButton('Own function')
        # self.radioButton_predev.setChecked(True)
        # self.radioButton_own.setChecked(loop_step.use_custom_fit)
        # self.radioButton_predev.clicked.connect(self.change_fitting)
        # self.radioButton_own.clicked.connect(self.change_fitting)
        #
        # self.comboBox_fit = QComboBox()
        # self.comboBox_fit.addItems(sorted(models_names.keys()))
        # if loop_step.predef_fit in models_names.keys():
        #     self.comboBox_fit.setCurrentText(loop_step.predef_fit)
        # else:
        #     self.comboBox_fit.setCurrentText('Linear')
        # self.lineEdit_fit_func = QLineEdit()
        # self.lineEdit_fit_func.setText(loop_step.custom_fit)
        # self.comboBox_fit.currentTextChanged.connect(self.change_fitting)
        # self.lineEdit_fit_func.textChanged.connect(self.change_fitting)
        #
        # cols = ['name', 'initial value']
        # self.start_params = AddRemoveTable(headerLabels=cols,
        #                                   title='Fit Parameters',
        #                                   editables=[1],
        #                                   tableData=loop_step.fit_params)
        # self.start_params.addButton.setHidden(True)
        # self.start_params.removeButton.setHidden(True)
        # self.change_fitting()

        self.layout().addWidget(label_sweep_channel, 1, 0)
        self.layout().addWidget(self.comboBox_sweep_channel, 1, 1, 1, 4)
        self.layout().addWidget(label_data, 2, 0)
        self.layout().addWidget(self.comboBox_data_output, 2, 1, 1, 4)
        self.layout().addWidget(self.sweep_widget, 5, 0, 1, 5)
        self.layout().addWidget(self.read_table, 6, 0, 1, 5)

        self.layout().addWidget(self.plot_widge, 8, 0, 1, 5)
        self.layout().addWidget(self.checkBox_use_own_plots, 7, 0, 1, 5)
        # self.layout().addWidget(self.plot_table, 7, 2, 1, 3)
        self.checkBox_use_own_plots.clicked.connect(self.use_plot_change)

        self.layout().addWidget(label_proc, 10, 0, 1, 5)
        self.layout().addWidget(self.checkBox_minmax, 11, 0, 1, 2)
        self.layout().addWidget(self.checkBox_mean, 11, 2, 1, 3)
        self.layout().addWidget(self.checkBox_stddev, 13, 0, 1, 2)
        # self.layout().addWidget(self.checkBox_fit, 20, 0, 1, 2)
        # self.layout().addWidget(self.checkBox_guess_fit, 20, 2, 1, 3)
        # self.layout().addWidget(self.radioButton_predev, 21, 0, 1, 2)
        # self.layout().addWidget(self.radioButton_own, 21, 2, 1, 3)
        # self.layout().addWidget(self.comboBox_fit, 22, 0, 1, 2)
        # self.layout().addWidget(self.lineEdit_fit_func, 22, 2, 1, 3)
        # self.layout().addWidget(self.start_params, 23, 0, 1, 5)


        self.use_plot_change()

    # def setup_plots(self):
    #     """Called when any preferences are changed. Makes the dictionary
    #      of preferences and calls save_preferences from the
    #      load_save_functions module."""
    #     plot_dialog = Plot_Definer(self)
    #     plot_dialog.exec_()
    #     print(plot_dialog.data)
    # if settings_dialog.exec_():
    #     self.preferences = settings_dialog.get_settings()
    #     number_formatting.preferences = self.preferences
    #     self.toggle_dark_mode()
    #     load_save_functions.save_preferences(self.preferences)
    #     variables_handling.device_driver_path = self.preferences['device_driver_path']
    #     variables_handling.meas_files_path = self.preferences['meas_files_path']
    # prefs = {'autosave': self.actionAutosave_on_closing.isChecked(),
    #          'dark_mode': self.actionDark_Mode.isChecked()}
    # load_save_functions.save_preferences(prefs)

    def use_plot_change(self):
        use_plots = self.checkBox_use_own_plots.isChecked()
        self.plot_widge.setEnabled(use_plots)




    def update_step_config(self):
        super().update_step_config()
        self.loop_step.use_own_plots = self.checkBox_use_own_plots.isChecked()
        self.loop_step.plots = self.plot_widge.plot_data
        # self.loop_step.plots = self.plot_table.update_table_data()
        self.loop_step.read_channels = self.read_table.get_info()['channel']
        self.loop_step.data_output = self.comboBox_data_output.currentText()
        self.loop_step.sweep_channel = self.comboBox_sweep_channel.currentText()
        self.loop_step.calc_minmax = self.checkBox_minmax.isChecked()
        self.loop_step.calc_mean = self.checkBox_mean.isChecked()
        self.loop_step.calc_stddev = self.checkBox_stddev.isChecked()
        # self.loop_step.calc_fit = self.checkBox_fit.isChecked()
        # self.loop_step.use_custom_fit = self.radioButton_own.isChecked()
        # self.loop_step.predef_fit = self.comboBox_fit.currentText()
        # self.loop_step.custom_fit = self.lineEdit_fit_func.text()


