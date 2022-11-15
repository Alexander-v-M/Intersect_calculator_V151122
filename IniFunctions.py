from configparser import ConfigParser

config = ConfigParser()
config.read('Data.ini')


class IniFunctions:

    def __init__(self):
        self.parameter_save_name = 'Unknown'
        self.list_ini_sections = config.sections()
        self.section_name = 'None'

    def get_sections(self):
        return self.list_ini_sections

    @staticmethod
    def _write(parameters_save_name, xp, min_x, max_x, eq1, eq2):
        config.add_section(f'{parameters_save_name}')
        config.set(f'{parameters_save_name}', 'x_points', f'{xp}')
        config.set(f'{parameters_save_name}', 'x_min', f'{min_x}')
        config.set(f'{parameters_save_name}', 'x_max', f'{max_x}')
        config.set(f'{parameters_save_name}', 'equation_1', f'{eq1}')
        config.set(f'{parameters_save_name}', 'equation_2', f'{eq2}')

        with open('Data.ini', 'w') as configfile:
            config.write(configfile)

    def update_config(self, update_con):
        self.list_ini_sections = config.sections()
        update_con()

    def write_to_ini(self, ent_par_sn, x_points, x_min, x_max, equation_1, equation_2, update_con, log_output):
        # write parameters to an ini file for later use.
        # if the entry for the save name is empty, save name will be 'Unknown'
        # if name is already used, save name is entry name with '(1)' added

        name_for_save = ent_par_sn
        if name_for_save != '':
            self.parameter_save_name = name_for_save

        try:
            self._write(self.parameter_save_name, x_points, x_min, x_max, equation_1, equation_2)
            self.update_config(update_con)
        except Exception:
            log_output

    @staticmethod
    def get_parameters_from_ini(section_name):

        equation_1 = config.get(f'{section_name}', 'equation_1')
        equation_2 = config.get(f'{section_name}', 'equation_2')
        x_points = config.getint(f'{section_name}', 'x_points')
        x_min = config.getint(f'{section_name}', 'x_min')
        x_max = config.getint(f'{section_name}', 'x_max')

        return x_points, x_min, x_max, equation_1, equation_2

    def del_ini_section(self, section_name, update_con):

        if section_name != 'None':
            config.remove_section(f'{section_name}')

            with open('Data.ini', 'w') as configfile:
                config.write(configfile)

            self.update_config(update_con)
