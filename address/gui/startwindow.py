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
        dialog = NewDialog(self.parent)
        if dialog.result is not None:
            self.parent.destroy()

    def importl(self):
        """
        creates a tab to place file path
        calls okay button
        need to fix to have self.path, different from
        file name for import
        """
        dialog = ImportDialog(self.parent)
        if dialog.result is not None:
            self.parent.destroy()

    def openfile(self):
        """
        Creates and OpenDialog and destroys this window.
        """
        dialog = OpenDialog(self.parent)
        if dialog.result is not None:
            self.parent.destroy()
