"""
The GUI module contains submodules for each type of window as well as a main
function to start the application.
"""
import Tkinter as tk

from address.constants import main_tk_root
from address.gui.startwindow import StartWindow


def main():
    """
    Launch the GUI.
    """
    root = tk.Tk()
    root.geometry("500x450+300+300")
    root.title("Team 2 Address Book")
    main_tk_root[1] = root
    main_tk_root[1].update()

    start_window = StartWindow(main_tk_root[1])

    main_tk_root[1].wait_window(start_window.top)

    main_tk_root[1].wait_window()

if __name__ == "__main__":
    main()
