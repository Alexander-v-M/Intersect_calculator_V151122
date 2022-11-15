from tkinter import *

from TwoLines import TwoLines
from PlotFunctions import PlotFunctions
from IniFunctions import IniFunctions

PF = PlotFunctions()


class Window:
    def __init__(self, root):
        """
        GUI Window for the intersect calculator
        """
        ##################################
        # settings for the GUI root
        self.width = 1165
        self.height = 550
        self.root = root
        self.root.title("Intersect Calculator")
        self.root.geometry(f'{self.width}x{self.height}')
        self.root.resizable(False, False)

        # starting parameters for the plot
        self.x_points = 50
        self.x_min = -10
        self.x_max = 10
        self.equation_1 = ''
        self.equation_2 = ''

        # additional plot settings
        self.intersect = False
        self.diff_1 = False
        self.diff_2 = False

        # set frames and widget to self
        self.frame1 = None
        self.frame2 = None
        self.frame3 = None
        self.frame3_1 = None
        self.frame3_2 = None

        # set entry variables to self
        self.ent_eq1 = None
        self.ent_eq2 = None
        self.ent_min_x = None
        self.ent_max_x = None
        self.ent_xp = None
        self.ent_intersect = BooleanVar()
        self.ent_diff_1 = BooleanVar()
        self.ent_diff_2 = BooleanVar()

        # ini parameters
        self.ent_save_name = ''
        self.section_name = 'None'
        self.option_var = StringVar()

        # text log parameters
        self.output_text = Text(self.frame3_2)

        ##################################
        # Initialise TwoLines class
        self.TL = TwoLines(self.equation_1, self.equation_2, self.x_points, self.x_min, self.x_max)

        # Initialise The window with frames and widgets
        self.frames_with_widgets()

        # configure matplotlib plot in frame2
        PF.set_plot(self.frame2)

    def frames_with_widgets(self):
        # Background for the GUI
        bg = '#49597a'

        # Divide the GUI in two frames
        self.frame1 = Frame(self.root, width=240, height=self.height, bg=bg)
        self.frame2 = Frame(self.root, width=675, height=self.height, bg='#f0f0f0')
        self.frame3 = Frame(self.root, width=240, height=self.height)
        self.frame3_1 = Frame(self.frame3, bg=bg, width=240, height=(self.height / 2))
        self.frame3_2 = Frame(self.frame3, bg=bg, width=240, height=(self.height / 2))

        self.frame1.pack(side="left", expand=True, fill='both')  # fill="both"
        self.frame2.pack(side="left", expand=True, fill='both')
        self.frame3.pack(side="right", expand=True, fill='both')
        self.frame3_1.pack(side="top", expand=True, fill='both')
        self.frame3_2.pack(side="bottom", expand=True, fill='both')

        # all the widgets and buttons

        ##################################
        # frame 1_1

        lx = 2
        ex = 90
        y_begin = 2
        y = y_begin
        plus_y = 25

        Label(self.frame1, text='Equation one: ', bg=bg, fg='white').place(x=lx, y=y)
        self.ent_eq1 = Entry(self.frame1, width=15)
        self.ent_eq1.place(x=ex, y=y)

        y += plus_y

        Label(self.frame1, text='Equation two: ', bg=bg, fg='white').place(x=lx, y=y)
        self.ent_eq2 = Entry(self.frame1, width=15)
        self.ent_eq2.place(x=ex, y=y)

        y += plus_y

        Label(self.frame1, text='X minimum: ', bg=bg, fg='white').place(x=lx, y=y)
        self.ent_min_x = Entry(self.frame1, width=15)
        self.ent_min_x.place(x=ex, y=y)

        y += plus_y

        Label(self.frame1, text='X maximum: ', bg=bg, fg='white').place(x=lx, y=y)
        self.ent_max_x = Entry(self.frame1, width=15)
        self.ent_max_x.place(x=ex, y=y)

        y += plus_y

        Label(self.frame1, text='Line quality: ', bg=bg, fg='white').place(x=lx, y=y)
        self.ent_xp = Entry(self.frame1, width=15)
        self.ent_xp.place(x=ex, y=y)

        y += plus_y

        plot_button = Button(self.frame1, text="Plot", command=lambda: self.plot_everything(log=False), width=25)
        plot_button.place(x=lx, y=y)
        self.frame1.bind("<Return>", self.plot_everything())

        ##################################
        # frame 1_2
        y = self.height / 2

        Checkbutton(self.frame1, text='Intersect', variable=self.ent_intersect,
                    bg=bg, fg='white', selectcolor='black').place(x=lx, y=y)

        y += plus_y

        Checkbutton(self.frame1, text='Derivative Eq1', variable=self.ent_diff_1,
                    bg=bg, fg='white', selectcolor='black').place(x=lx, y=y)

        y += plus_y

        Checkbutton(self.frame1, text='Derivative Eq2', variable=self.ent_diff_2,
                    bg=bg, fg='white', selectcolor='black').place(x=lx, y=y)

        y += plus_y

        update_values_button = Button(self.frame1, text="Update & Plot", command=self.plot_everything, width=14)
        update_values_button.place(x=lx, y=y)
        self.frame1.bind("<Return>", self.plot_everything())

        update_settings_button = Button(self.frame1, text="Load Settings", command=self.update_settings, width=10)
        update_settings_button.place(x=lx + 108, y=y)
        self.frame1.bind("<Return>", self.update_settings())

        ##################################
        # frame 3_1
        y = y_begin
        ex = 110

        Label(self.frame3_1, text='Enter save name: ', bg=bg, fg='white').place(x=lx, y=y)
        self.ent_save_name = Entry(self.frame3_1, width=15)
        self.ent_save_name.place(x=ex, y=y)

        y += plus_y

        save_button = Button(self.frame3_1, text="Save Parameters", width=28, command=self.ini_save_command)
        save_button.place(x=lx, y=y)
        self.frame3_1.bind("<Return>", self.ini_save_command)

        y += plus_y * 1.5

        Label(self.frame3_1, text='Load saved data: ', bg=bg, fg='white').place(x=lx, y=y)
        self.option_var.set(IniFunctions().get_sections()[0])
        self.option_var.trace("w", self.ini_update_section_name)
        menu = OptionMenu(self.frame3_1, self.option_var, *IniFunctions().get_sections())
        menu.config(borderwidth=-2)
        menu.place(x=ex, y=y, width=97)

        y += plus_y * 1.2

        load_button = Button(self.frame3_1, text="Load", width=14, command=self.ini_load_command)
        load_button.place(x=lx, y=y)
        self.frame3_1.bind("<Return>", self.ini_load_command)

        del_button = Button(self.frame3_1, text="Delete", width=12, command=self.ini_del_command)
        del_button.place(x=lx + 112, y=y)
        self.frame3_1.bind("<Return>", self.ini_del_command)

        ##################################
        # frame 3_2
        self.output_text = Text(self.frame3_2)
        self.output_text.insert('end', 'Welcome to the calculator')
        self.output_text.pack(side='top', fill='both', expand=1, padx=10, pady=10)

    def update_values(self):
        # update self.parameters by replacing the existing value by the entry value.
        self.equation_1 = str(self.ent_eq1.get())
        self.equation_2 = str(self.ent_eq2.get())

        try:
            self.x_points = int(self.ent_xp.get())
        except ValueError:
            pass

        try:
            self.x_min = int(self.ent_min_x.get())
        except ValueError:
            pass

        try:
            self.x_max = int(self.ent_max_x.get())
        except ValueError:
            pass

        self.TL = TwoLines(self.equation_1, self.equation_2, self.x_points, self.x_min, self.x_max)

    def update_settings(self, log=True):
        # update self.parameters by replacing the existing value by the entry value.
        try:
            self.intersect = bool(self.ent_intersect.get())
        except ValueError:
            pass

        try:
            self.diff_1 = bool(self.ent_diff_1.get())
        except ValueError:
            pass

        try:
            self.diff_2 = bool(self.ent_diff_2.get())
        except ValueError:
            pass

        # communicate to log
        if log is True:
            self.output_text.insert('end', 'Settings updated\n')
            # self.output_text.see('end')

    def plot_everything(self, update_values=True, log=True):
        # update entry values if true
        if update_values:
            self.update_values()

        # update settings
        self.update_settings(log=log)

        # set the plot en plot the lines
        PF.set_plot(self.frame2)
        PF.plot_lines(self.TL.get_y(), self.TL.x_list)

        # plot to intersect if true
        if self.intersect:
            intersect = self.TL.get_intersect()
            PF.show_intersect(intersect)

            # show in log
            self.output_text.insert('end', f'Coordinates intersection:\n{intersect}\n')

        if self.diff_1:
            PF.plot_diff(self.TL.get_diff(1), self.TL.get_x(), 1)

        if self.diff_2:
            PF.plot_diff(self.TL.get_diff(2), self.TL.get_x(), 2)

    def ini_save_command(self):
        # communicate to log
        self.output_text.insert('end', 'Parameters saved\n')

        # save to ini
        return IniFunctions().write_to_ini(
            self.ent_save_name.get(),
            self.x_points,
            self.x_min,
            self.x_max,
            self.equation_1,
            self.equation_2,
            self.ini_update_con,
            self.output_text.insert('end', 'Parameters saved failed.\nName already in use.\nEnter a new name.\n'))

    def ini_load_command(self):
        # get the parameters from the ini file and update self
        self.x_points, self.x_min, self.x_max, self.equation_1, self.equation_2 = \
            IniFunctions().get_parameters_from_ini(self.section_name)

        # update the calculation class
        self.TL = TwoLines(self.equation_1, self.equation_2, self.x_points, self.x_min, self.x_max)

        # communicate to log
        self.output_text.insert('end', 'Parameters loaded\n')

        # plot the ini parameters
        self.plot_everything(update_values=False, log=False)

    def ini_del_command(self):
        # communicate to log
        self.output_text.insert('end', 'Parameters deleted\n')
        return IniFunctions().del_ini_section(self.section_name, self.ini_update_con)

    def ini_update_section_name(self, *args):
        self.section_name = self.option_var.get()

    def ini_update_con(self):
        menu = OptionMenu(self.frame3_1, self.option_var, *IniFunctions().get_sections())
        menu.config(borderwidth=-2)
        menu.place(x=110, y=(2 + 25 + 25 * 1.5), width=97)
