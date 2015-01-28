"""
The GUI module contains submodules for each type of window as well as a main
function to start the application.
"""
import Tkinter as tk

from address.gui.startwindow import StartWindow


def main():
    """
    Launch the GUI.
    """
    root = tk.Tk()
    root.geometry("500x450+300+300")
    root.title("Address Book")
    StartWindow(root)
    tk.mainloop()


if __name__ == "__main__":
    main()
