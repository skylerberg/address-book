from Tkinter import *
from address.constants import *
from address.gui.startwindow import StartWindow


def main():
    root = Tk()
    root.geometry("500x450+300+300")    
    root.title("Team 2 Address Book")
    main_tk_root[1] = root
    main_tk_root[1].update()

    d = StartWindow(main_tk_root[1])

    main_tk_root[1].wait_window(d.top)

    main_tk_root[1].wait_window()

if __name__ == "__main__":
    main()
