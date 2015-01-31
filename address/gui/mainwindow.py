"""
Window for viewing and editing an address book.
"""
import Tkinter as tk
import tkFileDialog
import tkSimpleDialog
import tkFont
import os

from address.constants import *
from address.gui import dialogs
import address.data as data
from address import book
from address import entry
from address.gui import messagebox as mb
from address import utility


class MainWindow(object):
    """
    Main window class. This window displays the address book and allows the
    user to perform basic CRUD operations.
    """

    def __init__(self, name, action, import_path=None):
        if action == NEW:
            self.book = book.Book()
            self.book_saved  = False
        elif action == IMPORT:
            self.book = book.Book()
            self.book.import_from(import_path)
            self.book_saved  = False
        elif action == OPEN:
            self.book = data.load(name)
            self.book_saved  = True
        self.parent = tk.Tk()
        self.parent.geometry("1500x1250+300+300")
        self.parent.title("Address Book")
        self.parent.protocol('WM_DELETE_WINDOW', self.exit_handler)
        self.top = self.parent
        self.name = name
        self.value = ""
        self.e2 = ""
        self.elist=[]
        print name
        self.address=self.book.get_str_entries()
        self._menu = tk.Menu(self.parent, name='menu')
        self.build_submenus()
        self.top.config(menu=self._menu)
        self.show()

    def show(self):
        tk.Label(self.top,
                 text="Addresses Book "+self.name,
                 font=("Helvetica", 16)
                 ).pack(padx=5, pady=5)
        list_frame = tk.Frame(self.top)
        list_frame.pack(side=tk.TOP, padx=0, pady=0)
        scroll_bar = tk.Scrollbar(list_frame)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_bar2 = tk.Scrollbar(list_frame, orient=tk.HORIZONTAL)
        scroll_bar2.pack(side=tk.BOTTOM, fill=tk.X)
        self.list_box = tk.Listbox(list_frame, selectmode=tk.SINGLE, width=150, height=38, cursor="hand1")
        self.list_box.pack(side=tk.LEFT, fill=tk.Y)
        scroll_bar.config(command=self.list_box.yview)
        scroll_bar2.config(command=self.list_box.xview)
        self.list_box.config(yscrollcommand=scroll_bar.set)
        self.list_box.config(yscrollcommand=scroll_bar2.set)
        #self.address.sort()
        self.update_list()

    def build_submenus(self):
        self.add_file_menu()
        self.add_tool_menu()
        # the scroll click bar again here

    def add_file_menu(self):
        fmenu = tk.Menu(self._menu, name='muenu')
        self._menu.add_cascade(label='File', menu=fmenu, underline=0)
        labels = ('Open', 'New', 'Save', 'Save As', 'Import', 'Export', 'Merge')
        fmenu.add_command(label=labels[0], command=self.openl)
        fmenu.add_command(label=labels[1], command=self.newl)
        fmenu.add_command(label=labels[2], command=self.savel)
        fmenu.add_command(label=labels[3], command=self.saveasl)
        fmenu.add_command(label=labels[4], command=self.importl)
        fmenu.add_command(label=labels[5], command=self.exportl)
        fmenu.add_command(label=labels[6], command=self.mergel)

    def add_tool_menu(self):
        fmenu = tk.Menu(self._menu, name='fmenu')
        self._menu.add_cascade(label='Tools', menu=fmenu, underline=0)
        labels = ('Add entry',
                 'Delete entry',
                 'Edit entry',
                 'Search field',
                 'Print postal',
                 'Sort by',
                 'New Field')
        fmenu.add_command(label=labels[0], command=self.addE)
        fmenu.add_command(label=labels[1], command=self.deleteE)
        fmenu.add_command(label=labels[2], command=self.editE)
        fmenu.add_command(label=labels[3], command=self.searchE)
        fmenu.add_command(label=labels[4], command=self.printPostalE)
        fmenu.add_command(label=labels[5], command=self.sortbyE)
        fmenu.add_command(label=labels[6], command=self.newFieldE)

    def newFieldE(self):
        self.top = tk.Toplevel(self.parent)
        tk.Label(self.top, text="New Field").pack(padx=20, pady=10)

        self.e = tk.Entry(self.top)
        self.e.pack(padx=25)

        b = tk.Button(self.top, text="okay", command=self.fieldCheck)
        b.pack(pady=5)

    def fieldCheck(self):
        new_field = self.e.get()
    
        self.top.destroy()
        self.book.add_field(new_field)
        self.book_saved  = False

    def openl(self):
        dialogs.OpenDialog(self.parent)

    def newl(self):
        dialogs.NewDialog(self.parent)

    def mergel(self):
        self.top = tk.Toplevel(self.parent)
        list_frame = tk.Frame(self.top)
        scroll = tk.Scrollbar(list_frame)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        text = tk.Text(list_frame, yscrollcommand=scroll.set, width=45, height=20)
        text.pack()
        scroll.configure(command=text.yview)
        list_frame.pack()
        
        book_names = data.get_book_names()
        text.insert(tk.END, "\nHere is a list of the current address books:\n\n")
        for i in book_names:
             text.insert(tk.END, i+"\n")
        text.insert(tk.END, " \n\nBook 2 will be merged to Book 1. Please type the name of the books you want to merge.")
        tk.Label(self.top, text="Book 1").pack(padx=20, pady=10)
        self.e = tk.Entry(self.top)
        self.e.pack(padx=5)
        tk.Label(self.top, text="Book 2").pack(padx=20, pady=10)
        self.e2 = tk.Entry(self.top)
        self.e2.pack(padx=5)
        b = tk.Button(self.top, text="okay", command=self.okayMerge)
        b.pack(pady=5)


    def okayMerge(self):
        # open file one and file 2
        # then merger

        book_names = data.get_book_names()
        name1 = self.e.get()
        name2 = self.e2.get()
        if name1 in book_names and name2 in book_names and name1!=name2:
            self.top.destroy()
            print name1, name2
            b1 = data.load(name1)
            b2 = data.load(name2)
            b1.merge(b2)
            data.save(name1, b1)
            if self.name == name1:
                self.book =b1
                self.address = b1.get_str_entries()
                self.update_list()
                self.book_saved  = False
            print 'merging'
        if name1==name2 and name1 in book_names:
            mb.message(mb.WARNING,\
                    "Are you sure you  want to merge the same books together",\
                    parent=self.top)
        else:
            mb.message(mb.WARNING,\
                    "At least one of the books doesn't exist, make sure the book is saved before merging",\
                    parent=self.top)

    def saveasl(self):
        new_name = tkSimpleDialog.askstring("New name for the book", "new name", parent = self.parent)
        data.save(new_name, self.book)
        #self.book_saved  = True

    def savel(self):
        data.save(self.name, self.book)
        self.book_saved  = True
        print "Saving  book :" + self.name 

    def importl(self):
        dialogs.ImportDialog(self.parent)

    def exportl(self):
        self.export_path = tkFileDialog.asksaveasfilename(
                                    defaultextension=".tsv",
                                    filetypes=[("tab separate value","*.tsv")],
                                    initialdir = os.path.expanduser("~"),
                                    parent=self.parent
                                    ) 
        if self.export_path:
            print "exporting"
            self.book.export_to(range(len(self.book)),self.export_path)

    def addE(self):
        print "add"
        self.top = tk.Toplevel(self.parent)
        self.elist= []
        field_names = map(lambda field: DISPLAY_NAMES.get(field, field), self.book.get_fields())
        default_values = map(lambda field: DEFAULTS.get(field, ""), self.book.get_fields())
        for i in range(len(field_names)):
            tk.Label(self.top, text=field_names[i]).pack(padx=20, pady=10)
            self.elist.append(tk.Entry(self.top))
            self.elist[i].insert(0, default_values[i])
            self.elist[i].pack(padx=5)
        b = tk.Button(self.top, text="okay", command=self.getaddEntry)
        b.pack(pady=5)

    def getaddEntry(self):
        var = {}
        for i in range(len(self.book.get_fields())):
            var[self.book.get_fields()[i]] = self.elist[i].get()
        res = utility.has_invalid_field(var[ADDR].strip(),
                                        var[ZIP_CODE].strip(),
                                        var[PHONE_NUM].strip(),
                                        var[EMAIL].strip())
        if not res:
            entry_to_add = entry.Entry(**var)
            if entry_to_add not in self.book.entries:
                self.book.add_entry(entry_to_add)
                self.address = self.book.get_str_entries()
                self.list_box.insert(tk.END, self.address[-1])
                self.update_list()
                self.top.destroy()
                self.book_saved  = False
            else:
                mb.message(mb.WARNING, "Entry already exists!", parent=self.top)
        else:
            mb.message(mb.WARNING, ("%s is invalid!") % res, parent=self.top)

    def deleteE(self):
        try:
            first_index = self.list_box.curselection()[0]
            value = self.address[int(first_index)]
            if mb.message(mb.ASK,"Do you really want to delete it? There is no going back",parent=self.parent):
                entry_to_delete = self.to_entry(value)
                print entry_to_delete
                self.book.delete_entry(self.book.get_entry_index(entry_to_delete))
                self.address = self.book.get_str_entries()
                self.update_list()
                self.book_saved  = False
        except IndexError:
            mb.message(mb.WARNING,"Select an entry first!",parent=self.parent)

    def editE(self):
        try:
            first_index = self.list_box.curselection()[0]
        except IndexError:
            mb.message(mb.WARNING,"Select an entry first!",parent=self.parent)
        print 'index',first_index
        self.value = self.address[int(first_index)]
        self.top = tk.Toplevel(self.parent)
        self.elist= []
        field_names = map(lambda field: DISPLAY_NAMES.get(field, field), self.book.get_fields())
        for i in range(len(self.book.get_fields())):
            tk.Label(self.top, text=field_names[i]).pack(padx=20, pady=10)
            self.elist.append(tk.Entry(self.top))
            #if not field_names[i] in self.value:
            #    self.elist[i].insert(0,"")
            #else:
            self.elist[i].insert(0, self.value.split(DELIM)[i].split(":")[1])
            
            self.elist[i].pack(padx=5)
        self.index = int(first_index)
        b = tk.Button(self.top, text="okay", command=self.getEditEntry)
        b.pack(pady=5)

    def getEditEntry(self):
        var = {}
        for i in range(len(self.book.get_fields())):
            var[self.book.get_fields()[i]] = self.elist[i].get()
        res = utility.has_invalid_field(var[ADDR].strip(),
                                        var[ZIP_CODE].strip(),
                                        var[PHONE_NUM].strip(),
                                        var[EMAIL].strip())
        if not res:
            entry_pre = self.to_entry(self.value)
            entry_new = entry.Entry(**var)
            if entry_new not in self.book.entries:
                #delete old then add new
                self.book.delete_entry(self.book.get_entry_index(entry_pre))
                self.book.add_entry(entry_new)
                self.address = self.book.get_str_entries()
                self.list_box.delete(int(self.index))
                #self.list_box.insert(tk.END, self.address[self.index])
                self.list_box.insert(tk.END, str(entry_new))
                self.address.sort()
                self.update_list()
                self.top.destroy()
                self.book_saved  = False
                print self.address[self.index]
            else:
                mb.message(mb.WARNING,"Entry already exists!",parent=self.top)
        else:
            mb.message(mb.WARNING, ("%s is invalid!") % res, parent=self.top)

    def searchE(self):
        self.top = tk.Toplevel(self.parent)
        tk.Label(self.top, text="Field (optional)").pack(padx=20, pady=10)
        self.e = tk.Entry(self.top)
        self.e.pack(padx=5)
        tk.Label(self.top, text="Query").pack(padx=20, pady=10)
        self.e2 = tk.Entry(self.top)
        self.e2.pack(padx=5)
        b = tk.Button(self.top, text="search", command=self.search)
        b.pack(pady=5)
        print "search"

    def search(self):
        try:
            field = self.e.get()
            item_search = self.e2.get()
            print field + " " +item_search
            matches = self.book.search(item_search,field)
            sub_book = book.Book()
            sub_book.set_entries(matches)
            self.address = sub_book.get_str_entries()
            self.top.destroy()
            self.update_list()
        except KeyError:
            mb.message(mb.WARNING,"This field doesn't exist. Leave it blank or input a valid one.",parent=self.top)

    def printPostalE(self):
        try:
            first_index = self.list_box.curselection()[0]
        except IndexError:
            mb.message(mb.WARNING,"Select an entry first!",parent=self.parent)
        value = self.address[int(first_index)]
        entry_to_print = self.to_entry(value)
        index = self.book.get_entry_index(entry_to_print)
        postal = self.book.get_entry(index).to_postal()
        print postal
        self.top = tk.Toplevel(self.parent)
        for line in postal:
            tk.Label(self.top, text=line).pack(padx=20, pady=10)

    def sortbyE(self):
        selection_box = dialogs.PickAttribute(self.parent, self.book)
        if selection_box.result is not None:
            self.book.sort(selection_box.result)
            self.address = self.book.get_str_entries()
            self.update_list()

    def to_entry(self,value):
        '''
        Reconstruct an entry object from the selected string.

        :arg value: The string representing an entry in the book
        :type value: String

        :returns: An Entry object
        :rtypes: Entry
        '''
        attrs = []
        for i in range(len(self.book.get_fields())):
            attrs.append(value.split(DELIM)[i].split(":")[1])
        return entry.Entry(*attrs)

    def update_list(self):
        '''
        Refresh the list box in the gui.
        '''
        self.list_box.delete(0,tk.END)
        strings =""
        entries = []
        for value in self.address:
            entries.append(self.to_entry(value))

        #for item in self.book.entries:
        for item in entries:
            for key in item.__dict__.keys():
                strings += key +":  {" + key + "}"
                added_distance = 45+len(key)
                if (added_distance ==45):
                    added_distance = 50
                strings += (" " * added_distance)
            time= strings.format(**item.__dict__)
            self.list_box.insert(tk.END,time)
            strings=""

    def exit_handler(self):
        '''
        Customized handler for closing window event.
        This is used for checking if a user closes window before saving the book
        '''
        if not self.book_saved:
            discard = mb.message(mb.ASK,\
                    "Changes are not saved yet. Do you want to discard the changes?" \
                    "\n('Yes' to discard changes and quit, 'No' to go back ) ",\
                    parent = self.parent)
            if discard:
                self.parent.destroy()
        else:
            self.parent.destroy()
