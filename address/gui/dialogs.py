"""
Dialogs that can be accessed by any windows.
"""
import os
import Tkinter as tk
import tkFileDialog

from address.constants import OPEN, NEW, IMPORT
import address.gui
import address.data as data
from address.gui import messagebox as mb



class OpenDialog(tk.Toplevel):
    """
    Dialog for opening an existing address book.
    """

    def __init__(self, parent, title=None):
        tk.Toplevel.__init__(self, parent)
        self.result = None
        if title is not None:
            self.title = title

        self.parent = parent

        self.bind("<Return>", self._open)
        tk.Label(self, text="Open address book").pack(padx=5, pady=5)
        list_frame = tk.Frame(self)
        list_frame.pack(side=tk.TOP, padx=5, pady=5)
        scroll_bar = tk.Scrollbar(list_frame)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.list_box = tk.Listbox(list_frame, selectmode=tk.SINGLE)
        self.list_box.pack(side=tk.LEFT, fill=tk.Y)
        scroll_bar.config(command=self.list_box.yview)
        self.list_box.config(yscrollcommand=scroll_bar.set)

        self.metadata = data.get_book_names()

        for item in self.metadata:
            self.list_box.insert(tk.END, item)
        button_frame = tk.Frame(self)
        button_frame.pack(side=tk.BOTTOM)
        open_button = tk.Button(button_frame,
                                  text="Open",
                                  command=self._open)
        open_button.pack()
        cancel_button = tk.Button(button_frame,
                                  text="Cancel",
                                  command=self.destroy)
        cancel_button.pack()


        self.grab_set()
        self.parent.wait_window(self)

    def _open(self, *args):
        """
        Open the address book selected by the user.
        """
        #TODO handle no selection
        selected_index = self.list_box.curselection()[0]
        name = self.metadata[int(selected_index)]
        self.destroy()
        try:
            self.result = address.gui.MainWindow(name, OPEN)
        except IOError:
            mb.message(mb.ERROR,"File doesn't exist!",parent=self.parent)


class NewDialog(tk.Toplevel):
    """
    Dialog for creating a new address book.
    """

    def __init__(self, parent, title=None):
        tk.Toplevel.__init__(self, parent)
        if title is not None:
            self.title = title
        self.parent = parent
        self.result = None

        self.bind("<Return>", self._open)

        tk.Label(self, text="BookName").pack(padx=20, pady=10)

        self.e = tk.Entry(self)
        self.e.pack(padx=25)

        okay_button = tk.Button(self, text="okay", command=self._open)
        okay_button.pack(pady=5)

        self.grab_set()
        self.e.focus_set()
        self.parent.wait_window(self)

    def _open(self, *args):
        """
        Open the address book selected by the user.
        """
        name = self.e.get()
        if name not in data.get_book_names():
            self.destroy()
            self.result = address.gui.MainWindow(name, NEW)
        else:
            mb.message(mb.WARNING, ("There is already a book named %s, new name pls!") % name, parent=self.parent)


class ImportDialog(tk.Toplevel):
    """
    Dialog for importing an address book from a file.
    """

    def __init__(self, parent, title=None):
        self.result = None
        self.import_path = tkFileDialog.askopenfilename(
                                defaultextension=".tsv",
                                filetypes=[("tab separated values", "*.tsv")],
                                initialdir=os.path.expanduser("~"),
                                parent=parent
                                )
        if self.import_path:
            tk.Toplevel.__init__(self, parent)
            if title is not None:
                self.title = title
            self.parent = parent

            self.bind("<Return>", self._open)
            tk.Label(self, text="BookName").pack(padx=20, pady=10)
            self.e = tk.Entry(self)
            self.e.pack(padx=5)
            b = tk.Button(self, text="okay", command=self._open)
            b.pack(pady=5)
            self.grab_set()
            self.e.focus_set()
            self.parent.wait_window(self)


    def _open(self, *args):
        """
        Open the address book selected by the user.
        """
        name = self.e.get()
        if name not in data.get_book_names():
            self.destroy()
            try:
                self.result = address.gui.MainWindow(name, IMPORT, self.import_path)
            except ValueError:
                mb.message(mb.ERROR,"File is corrupted!",parent=self.parent)
        else:
            mb.message(mb.WARNING, ("There is already a book named %s, new name pls!") % name, parent=self.parent)
