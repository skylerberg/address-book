"""
The GUI module contains submodules for each type of window as well as a main
function to start the application.
"""
import Tkinter as tk
import os

from address.constants import main_tk_root
from address.gui.startwindow import StartWindow
from address.gui.mainwindow import MainWindow
from address import utility



def main():
    """
    Launch the GUI.
    """
    root = tk.Tk()
    root.geometry("500x450+300+300")
    root.title("Team 2 Address Book")
    main_tk_root[1] = root
    main_tk_root[1].update()

    data_dir = os.path.expanduser("~")+"/.address"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    os.chdir(data_dir)

    start_window=StartWindow(main_tk_root[1])

    tk.mainloop()


if __name__ == "__main__":
    main()
