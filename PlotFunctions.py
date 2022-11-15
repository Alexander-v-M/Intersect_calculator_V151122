import matplotlib.pyplot as plt
from tkinter import Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


# NotImplementedError: could not solve 2**(-sqrt(5)*sqrt(4*y - 31)/10 + 1/2) - y
class PlotFunctions:
    """
    A few plot functions for the main window widget
    """

    def set_plot(self, root):
        # delete existing plot
        self._clear(root)

        # plot style
        plt.style.use('bmh')

        # Initialise plot figure
        figure = plt.figure(figsize=(7, 5), dpi=100)
        figure.add_subplot(111)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')

        # Place plot into frame2
        chart = FigureCanvasTkAgg(figure, root)
        chart.get_tk_widget().pack(side='top', fill='both', expand=1)  # (side='top')

        # Settings for the navigation toolbar
        toolbar = NavigationToolbar2Tk(chart, root, pack_toolbar=False)
        # toolbar.config(background="black")
        # toolbar._message_label.config(background="black", fg='white')
        # toolbar.winfo_children()[9].config(background="black")
        # toolbar.winfo_children()[10].config(background="black")
        toolbar.pack(side='left')

    @staticmethod
    def _clear(frame):
        for child in frame.winfo_children():
            child.destroy()

    @staticmethod
    def plot_lines(get_y, x_list):
        # plot the lines from the TwoLines class into the plot
        # check if y list is empty (no equations has been entered)
        sol_1, sol_2 = get_y
        for i in [[sol_1, '#5a30ff'], [sol_2, '#ff4d17']]:
            if len(i[0]) != 0:
                plt.plot(x_list, i[0], color=i[1])
            else:
                plt.plot([], i[0])

    @staticmethod
    def show_intersect(get_intersect):
        # If an intersect is present and the option is turned on, display intersect coordinates in plot.
        cor = get_intersect
        if cor != 'No intersect':
            for i in cor:
                plt.plot(i[0], i[1], marker="o", markersize=3)
                round_1, round_2 = round(i[0], 2), round(i[1], 2)
                plt.annotate(f'({round_1}; {round_2})', (i[0], i[1]))

    @staticmethod
    def plot_diff(y_diff, x_list, eq):
        if eq == 1:
            color_line = '#5a30ff'
        elif eq == 2:
            color_line = '#ff4d17'

        if len(y_diff) > 1:
            plt.plot(x_list, y_diff, ls='--', color=color_line)
        else:
            plt.plot([], [])


