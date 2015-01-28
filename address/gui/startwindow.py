"""
Initial window when the application is launched.
"""
import Tkinter as tk
import tkFileDialog
import os

#from address.constants import main_tk_root
from address.constants import *
from address.gui.mainwindow import MainWindow
from address.gui.dialogs import OpenDialog
from address import book

class StartWindow(object):
    """
    First window that allows users to create, import or open address books.
    """

    def __init__(self, parent):
        self.parent = parent
        self.top = self.parent

        self.name = ""
        print self.name
        new_button = tk.Button(parent,
                               text="new",
                               command=self.new, height=5, width=20)
        new_button.pack(pady=30)
        open_button = tk.Button(parent,
                                text="openfile",
                                command=self.openfile, height=5, width=20)
        open_button.pack(pady=30)
        import_button = tk.Button(parent,
                                  text="import",
                                  command=self.importl, height=5, width=20)
        import_button.pack(pady=30)

    def new(self):
        """
        creates a tab to place file name
        calls okay button
        """
#
        self.action = NEW
#
        self.top = tk.Toplevel(self.parent)
        tk.Label(self.top, text="BookName").pack(padx=20, pady=10)

        self.e = tk.Entry(self.top)
        self.e.pack(padx=25)

        okay_button = tk.Button(self.top, text="okay", command=self.okay)
        okay_button.pack(pady=5)
        self.top.grab_set()
        self.parent.wait_window(self.top)

    def importl(self):
        """
        creates a tab to place file path
        calls okay button
        need to fix to have self.path, different from
        file name for import
        """
#
        self.action = IMPORT

        self.import_path = tkFileDialog.askopenfilename(
                                    defaultextension=".tsv",
                                    filetypes=[("tab separate value","*.tsv")],
                                    initialdir = os.path.expanduser("~"),
                                    parent=self.parent
                                    ) 
        if self.import_path:
            self.top = tk.Toplevel(self.parent)
            tk.Label(self.top, text="BookName").pack(padx=20, pady=10)
            self.e = tk.Entry(self.top)
            self.e.pack(padx=5)
            b = tk.Button(self.top, text="okay", command=self.okay)
            b.pack(pady=5)
#
        #print"Need to access file path call our import function"
        #tk.Label(self.top, text="FileName").pack(padx=20, pady=10)
        #self.e2 = tk.Entry(self.top)
        #self.e2.pack(padx=5)

    def openfile(self):
        """
        Creates and OpenDialog and destroys this window.
        """
        OpenDialog(self.parent)
        # TODO: Only destroy if it was not cancelled
        self.parent.destroy()

    def openl(self):
        """
        gets name and can use it to get data file, need to open file
        creates a new window deletes the old
        New window will have file data uploaded on page
        """
        # open file and placedata in after d.address = all entries
        root2 = tk.Tk()
        root2.geometry("1500x1250+300+300")
        root2.title("Team 2 Address Book")
        main_tk_root[1].destroy()
        main_tk_root[1] = root2
        main_tk_root[1].update()
        self.parent = root2

        if self.action == IMPORT:
            MainWindow(main_tk_root[1],self.name,self.action,self.import_path)
        else:
            MainWindow(main_tk_root[1],self.name,self.action)

    def okay(self):
        """
        grabs name for file
        destorys the window
        opens the file
        """
#seems okay has to do with new name(new or import)
        self.name = self.e.get()

        self.top.destroy()
        self.openl()
