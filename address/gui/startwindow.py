"""
Initial window when the application is launched.
"""
import Tkinter as tk
import tkFileDialog

#from address.constants import main_tk_root
from address.constants import *
from address.gui.mainwindow import MainWindow
from address import book

class StartWindow(object):
    """
    First window that allows users to create, import or open address books.
    """

    def __init__(self, parent, metadata):
        self.parent = parent
        self.top = self.parent
#
        self.metadata = metadata#["a", "aa"]# this is our metadata file

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
        tk.Label(self.top, text="FileName").pack(padx=20, pady=10)

        self.e = tk.Entry(self.top)
        self.e.pack(padx=25)

        okay_button = tk.Button(self.top, text="okay", command=self.okay)
        okay_button.pack(pady=5)

    def importl(self):
        """
        creates a tab to place file path
        calls okay button
        need to fix to have self.path, different from
        file name for import
        """
#
        self.action = IMPORT
#
        print"Need to access file path call our import function"
        self.top = tk.Toplevel(self.parent)
        tk.Label(self.top, text="File Path").pack(padx=20, pady=10)
        self.e = tk.Entry(self.top)
        self.e.pack(padx=5)
        tk.Label(self.top, text="FileName").pack(padx=20, pady=10)
        self.e2 = tk.Entry(self.top)
        self.e2.pack(padx=5)
        b = tk.Button(self.top, text="okay", command=self.okay)
        b.pack(pady=5)

    def openfile(self):
        """
        this gets the metadata file name and propertys
        """
#
        self.action = IMPORT
#
        if self.name == "":
            print " need to access file from metadata" + self.name
            self.top = tk.Toplevel(self.parent)
            self.top.grab_set()
            self.top.bind("<Return>", self._choose)
            tk.Label(self.top, text="open file").pack(padx=5, pady=5)
            list_frame = tk.Frame(self.top)
            list_frame.pack(side=tk.TOP, padx=5, pady=5)
            scroll_bar = tk.Scrollbar(list_frame)
            scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
            self.list_box = tk.Listbox(list_frame, selectmode=tk.SINGLE)
            self.list_box.pack(side=tk.LEFT, fill=tk.Y)
            scroll_bar.config(command=self.list_box.yview)
            self.list_box.config(yscrollcommand=scroll_bar.set)
            self.metadata.sort()

            for item in self.metadata:
                self.list_box.insert(tk.END, item)
            button_frame = tk.Frame(self.top)
            button_frame.pack(side=tk.BOTTOM)
            choose_button = tk.Button(button_frame,
                                      text="Choose",
                                      command=self._choose)
            choose_button.pack()
            cancel_button = tk.Button(button_frame,
                                     text="Cancel",
                                     command=self._cancel)
            cancel_button.pack(side=tk.RIGHT)

        else:
            print self.name + "a new file or imported file"

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

        MainWindow(main_tk_root[1],self.name,self.metadata,self.action)

    def _choose(self, event=None):
        """
        Chooses correct file to open
        """
        try:
            first_index = self.list_box.curselection()[0]
            value = self.metadata[int(first_index)]
            self.top.destroy()
            self.name = value
            self.openl()
        except IndexError:
            #print "here"
            self.name = None
            self.top.destroy()

    def _cancel(self, event=None):
        """ if not right close and they need to reopen"""
        self.top.destroy()

    def okay(self):
        """
        grabs name for file
        destorys the window
        opens the file
        """
#seems okay has to do with new name
        self.name = self.e.get()
        if not self.name in self.metadata:
            self.metadata.append(self.name)
        else:
#what to do
            pass

        self.top.destroy()
        self.openl()
