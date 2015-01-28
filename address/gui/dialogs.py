"""
Dialogs that can be accessed by any windows.
"""
import Tkinter as tk

from address import utility
from address.constants import OPEN
import address.gui


class OpenDialog(tk.Toplevel):
    """
    Dialog for opening an existing address book.
    """

    def __init__(self, parent, title=None):
        tk.Toplevel.__init__(self, parent)
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

        self.metadata = utility.get_metadata()
        self.metadata.sort()

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

    def _open(self):
        """
        Open the address book selected by the user.
        """
        #TODO handle no selection
        selected_index = self.list_box.curselection()[0]
        name = self.metadata[int(selected_index)]
        self.destroy()
        new_root = tk.Tk()
        new_root.geometry("1500x1250+300+300")
        new_root.title("Team 2 Address Book")
        address.gui.MainWindow(new_root, name, self.metadata, OPEN)
