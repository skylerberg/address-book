"""
Dialogs that can be accessed by any windows.
"""
import os
import Tkinter as tk
import tkFileDialog

from address.constants import *
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
        try:
            selected_index = self.list_box.curselection()[0]
            name = self.metadata[int(selected_index)]
            self.destroy()
            self.result = address.gui.MainWindow(name, OPEN)
        except IOError:
            mb.message(mb.ERROR,"Cannot open the file!",parent=self.parent)
        except IndexError:
            mb.message(mb.WARNING,"Please select a book!",parent=self)



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

        tk.Label(self, text="Book name").pack(padx=20, pady=10)

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
        if name not in data.get_book_names() and len(name.strip()) > 0:
            self.result = address.gui.MainWindow(name, NEW)
            self.destroy()
        elif len(name.strip()) == 0:
            mb.message(mb.WARNING, "Book name cannot be empty!", parent=self.parent)
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
            tk.Label(self, text="Book name").pack(padx=20, pady=10)
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
        if name not in data.get_book_names() and len(name.strip()) > 0:
            self.destroy()
            try:
                self.result = address.gui.MainWindow(name, IMPORT, self.import_path)
            except ValueError:
                mb.message(mb.ERROR,"File is corrupted!",parent=self.parent)
        elif len(name.strip()) == 0:
            mb.message(mb.WARNING, "Book name cannot be empty!", parent=self.parent)
        else:
            mb.message(mb.WARNING, ("There is already a book named %s, new name pls!") % name, parent=self.parent)


class PickAttribute(tk.Toplevel):

    def __init__(self, parent, book):
        tk.Toplevel.__init__(self, parent)
        self.result = None
        self.parent = parent

        self.bind("<Return>", self._select)
        tk.Label(self, text="Select attribute").pack(padx=5, pady=5)
        list_frame = tk.Frame(self)
        list_frame.pack(side=tk.TOP, padx=5, pady=5)
        scroll_bar = tk.Scrollbar(list_frame)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.list_box = tk.Listbox(list_frame, selectmode=tk.SINGLE)
        self.list_box.pack(side=tk.LEFT, fill=tk.Y)
        scroll_bar.config(command=self.list_box.yview)
        self.list_box.config(yscrollcommand=scroll_bar.set)

        for attribute in book.get_fields():
            self.list_box.insert(tk.END, DISPLAY_NAMES.get(attribute, attribute))
        self.book = book
        button_frame = tk.Frame(self)
        button_frame.pack(side=tk.BOTTOM)
        select_button = tk.Button(button_frame,
                                  text="Select",
                                  command=self._select)
        select_button.pack()
        cancel_button = tk.Button(button_frame,
                                  text="Cancel",
                                  command=self.destroy)
        cancel_button.pack()

        self.grab_set()
        self.parent.wait_window(self)

    def _select(self, *args):
        """
        Select an attribute.
        """
        try:
            selected_index = self.list_box.curselection()[0]
            field = self.book.get_fields()[int(selected_index)]
            self.result = NON_DISPLAY_NAMES.get(field, field)
            self.destroy()
        except:
            mb.message(mb.WARNING,"Please select an attribute!",parent=self)

