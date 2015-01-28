"""
Initial window when the application is launched.
"""
import Tkinter as tk

from address.gui.dialogs import OpenDialog, NewDialog, ImportDialog

class StartWindow(object):
    """
    First window that allows users to create, import or open address books.
    """

    def __init__(self, parent):
        self.parent = parent
        new_button = tk.Button(parent,
                               text="New",
                               command=self.new, height=5, width=20)
        new_button.pack(pady=30)
        open_button = tk.Button(parent,
                                text="Open",
                                command=self.open, height=5, width=20)
        open_button.pack(pady=30)
        import_button = tk.Button(parent,
                                  text="Import",
                                  command=self.import_, height=5, width=20)
        import_button.pack(pady=30)

    def new(self):
        """
        Creates an NewDialog and destroys this window if a new book is created.
        """
        dialog = NewDialog(self.parent)
        if dialog.result is not None:
            self.parent.destroy()

    def import_(self):
        """
        Creates an ImportDialog and destroys this window if a book is imported.
        """
        dialog = ImportDialog(self.parent)
        if dialog.result is not None:
            self.parent.destroy()

    def open(self):
        """
        Creates an OpenDialog and destroys this window if a book is opened.
        """
        dialog = OpenDialog(self.parent)
        if dialog.result is not None:
            self.parent.destroy()
