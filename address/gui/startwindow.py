import address.book as book
import Tkinter as tk
import tkFileDialog
from address.constants import *
from address.gui.mainwindow import MainWindow

class StartWindow:

    def __init__(self, parent):
        self.parent = parent
        self.top = self.parent
        self.metadata = ["a", "aa"]# this is our metadata file

        self.name = ""
        print self.name
        b = tk.Button(parent, text="new", command=self.new, height=5, width=20)
        b.pack(pady=30)
        b = tk.Button(parent, text="openfile", command=self.openfile, height=5, width=20)
        b.pack(pady=30)
        b = tk.Button(parent, text="import", command=self.importl, height=5, width=20)
        b.pack(pady=30)

    def new(self):
        """
        creates a tab to place file name
        calls okay button
        """
        self.top = tk.Toplevel(self.parent)
        tk.Label(self.top, text="FileName").pack(padx=20, pady=10)

        self.e = tk.Entry(self.top)
        self.e.pack(padx=25)

        b = tk.Button(self.top, text="okay", command=self.okay)
        b.pack(pady=5)

    def importl(self):
        """
        creates a tab to place file path
        calls okay button
        need to fix to have self.path, different from
        file name for import
        """
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
        if self.name == "":
            print " need to access file from metadata" + self.name
            self.top = tk.Toplevel(self.parent)
            self.top.grab_set()
            self.top.bind("<Return>", self._choose)
            tk.Label(self.top, text="open file").pack(padx=5, pady=5)
            listFrame = tk.Frame(self.top)
            listFrame.pack(side=tk.TOP, padx=5, pady=5)
            scrollBar = tk.Scrollbar(listFrame)
            scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
            self.listBox = tk.Listbox(listFrame, selectmode=tk.SINGLE)
            self.listBox.pack(side=tk.LEFT, fill=tk.Y)
            scrollBar.config(command=self.listBox.yview)
            self.listBox.config(yscrollcommand=scrollBar.set)
            self.metadata.sort()

            for item in self.metadata:
                self.listBox.insert(tk.END, item)
            buttonFrame = tk.Frame(self.top)
            buttonFrame.pack(side=tk.BOTTOM)
            chooseButton = tk.Button(buttonFrame, text="Choose", command=self._choose)
            chooseButton.pack()
            cancelButton = tk.Button(buttonFrame, text="Cancel", command=self._cancel)
            cancelButton.pack(side=tk.RIGHT)

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

        d = MainWindow(main_tk_root[1], self.name, self.metadata)

    def _choose(self, event=None):
        """
        Chooses correct file to open
        """
        try:
            firstIndex = self.listBox.curselection()[0]
            value = self.metadata[int(firstIndex)]
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
        self.name = self.e.get()
        self.top.destroy()
        self.openl()
