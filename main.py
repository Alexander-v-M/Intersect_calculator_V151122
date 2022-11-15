from tkinter import Tk, messagebox
from Window2 import Window


def main():
    root = Tk()
    gui = Window(root)

    def when_quit():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()
            root.quit()

    root.protocol("WM_DELETE_WINDOW", when_quit)

    gui.root.mainloop()


if __name__ == "__main__":
    main()
