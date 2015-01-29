"""
Window for viewing and editing an address book.
"""
import Tkinter as tk
import tkFileDialog
import tkSimpleDialog
import os

from address.constants import *
from address.gui.dialogs import OpenDialog, NewDialog, ImportDialog, PickAttribute
import address.data as data
from address import book
from address import entry
from address.gui import messagebox as mb


class MainWindow(object):
    """
    Main window class. This window displays the address book and allows the
    user to perform basic CRUD operations.
    """

#
    def __init__(self, name, action, import_path=None):#since import_path is likely to be different from name..
        if action == NEW:
            self.book = book.Book()
            #print 'here',name,action
        elif action == IMPORT:
            self.book = book.Book()
            self.book.import_from(import_path)
        elif action == OPEN:
            self.book = data.load(name)
#
        self.parent = tk.Tk()
        self.parent.geometry("1500x1250+300+300")
        self.parent.title("Address Book")
        self.top = self.parent
        self.name = name
        self.value = ""
        self.e2 = ""
        self.elist=[]
        print name
        self.address=self.book.get_str_entries() #["name1, address1, phone1","name2, address2, phone2"]
        #self.top = Toplevel(self.parent)
        self._menu = tk.Menu(self.parent, name='menu')
        self.build_submenus()
        self.top.config(menu=self._menu)
        #self.top.grab_set()
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
        self.list_box = tk.Listbox(list_frame, selectmode=tk.SINGLE, width=150, height=38)
        self.list_box.pack(side=tk.LEFT, fill=tk.Y)
        scroll_bar.config(command=self.list_box.yview)
        self.list_box.config(yscrollcommand=scroll_bar.set)
        self.address.sort()

        for item in self.address:
            self.list_box.insert(tk.END, item)

    def build_submenus(self):
        self.add_file_menu()
        self.add_tool_menu()
        # the scroll click bar again here

    def add_file_menu(self):
        fmenu = tk.Menu(self._menu, name='muenu')
        self._menu.add_cascade(label='File', menu=fmenu, underline=0)
        labels = ('Open', 'New', 'Save', 'Save As', 'Import', 'Export', "Merge")
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

    def openl(self):
        OpenDialog(self.parent)

    def newl(self):
        """
        creates a tab to place file name
        calls okay button
        """
        NewDialog(self.parent)

    def mergel(self):
        self.top = tk.Toplevel(self.parent)
        tk.Label(self.top, text="File1").pack(padx=20, pady=10)
        self.e = tk.Entry(self.top)
        self.e.pack(padx=5)
        tk.Label(self.top, text="File2").pack(padx=20, pady=10)
        self.e2 = tk.Entry(self.top)
        self.e2.pack(padx=5)
        b = tk.Button(self.top, text="okay", command=self.okayMerge)
        b.pack(pady=5)

    def okayMerge(self):
        # open file one and file 2
        # then merger
#e exception
        name1 = self.e.get()
        name2 = self.e2.get()
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
        elif self.name == name2:
#e what to do? close window?
                pass
#
        print 'merging'

    def saveasl(self):
        new_name = tkSimpleDialog.askstring("New name for the book", "new name", parent = self.parent)
        data.save(new_name, self.book)

    def savel(self):
        data.save(self.name, self.book)

    def importl(self):
        """
        creates a tab to place file path
        need to fix to have self.path, different from
        file name for import
        """
        ImportDialog(self.parent)

    def exportl(self):
        #self.top = tk.Toplevel(self.parent)
        self.export_path = tkFileDialog.asksaveasfilename(
                                    defaultextension=".tsv",
                                    filetypes=[("tab separate value","*.tsv")],
                                    initialdir = os.path.expanduser("~"),
                                    parent=self.parent
                                    ) 
        if self.export_path:
            self.exportfile()
        #tk.Label(self.top, text="File Path").pack(padx=20, pady=10)
        #self.e = tk.Entry(self.top)

        #self.e.pack(padx=5)
        #tk.Label(self.top, text="FileName").pack(padx=20, pady=10)
        #self.e2 = tk.Entry(self.top)
        #self.e2.pack(padx=5)
        #b = tk.Button(self.top, text="okay", command=self.exportfile)
        #b.pack(pady=5)

    def exportfile(self):
        print "exporting"
        self.book.export_to(range(len(self.book)),self.export_path)
        #self.top.destroy()

    def addE(self):
        print "add"
        self.top = tk.Toplevel(self.parent)
        self.elist= []
        for i in range(len(self.book.get_fields())):
            tk.Label(self.top, text=self.book.get_fields()[i]).pack(padx=20, pady=10)
            self.elist.append(tk.Entry(self.top))
            self.elist[i].insert(0, self.book.get_fields()[i])
            self.elist[i].pack(padx=5)
        b = tk.Button(self.top, text="okay", command=self.getaddEntry)
        b.pack(pady=5)

    def getaddEntry(self):
        var = []
        for i in range(len(self.listFields)):
            var.append(self.elist[i].get())

        entry_to_add = entry.Entry(*var)
        if entry_to_add not in self.book.entries:
            self.book.add_entry(entry_to_add)
            self.address = self.book.get_str_entries()
            self.list_box.insert(tk.END, self.address[-1])
            self.update_list()
            self.top.destroy()
        else:
            mb.message(mb.WARNING,"Entry already exists!",parent=self.top)

    def deleteE(self):
        first_index = self.list_box.curselection()[0]
        value = self.address[int(first_index)]
#
        entry_to_delete = self.to_entry(value)
        self.book.delete_entry(self.book.get_entry_index(entry_to_delete))
        self.address = self.book.get_str_entries()
        self.update_list()
#
        print value
        #self.address.pop(int(first_index))
        #self.deleteShow()
        #self.show()
        #self.list_box.delete(int(first_index))
        print self.address

    def editE(self):
        
        first_index = self.list_box.curselection()[0]
        print 'index',first_index
        #print self.address[first_index]
        self.value = self.address[int(first_index)]
        self.top = tk.Toplevel(self.parent)
        self.elist= []
        for i in range(len(self.book.get_fields())):
            tk.Label(self.top, text=self.book.get_fields()[i]).pack(padx=20, pady=10)
            self.elist.append(tk.Entry(self.top))
##
            self.elist[i].insert(0, self.book.get_fields()[i])
            self.elist[i].pack(padx=5)
        #print self.elist
        self.index = int(first_index)
        b = tk.Button(self.top, text="okay", command=self.getEditEntry)
        b.pack(pady=5)

    def getEditEntry(self):
#
        var = []
        for i in range(len(self.book.get_fields())):
            var.append(self.elist[i].get())

        entry_pre = self.to_entry(self.value)
        entry_new = entry.Entry(*var)
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
            print self.address[self.index]
        else:
            mb.message(mb.WARNING,"Entry already exists!",parent=self.top)
#

    def searchE(self):
        self.top = tk.Toplevel(self.parent)
        tk.Label(self.top, text="Field").pack(padx=20, pady=10)
        self.e = tk.Entry(self.top)
        self.e.pack(padx=5)
        tk.Label(self.top, text="quere").pack(padx=20, pady=10)
        self.e2 = tk.Entry(self.top)
        self.e2.pack(padx=5)
        b = tk.Button(self.top, text="search", command=self.search)
        b.pack(pady=5)
        print "search"

    def search(self):
        field = self.e.get()
        item_search = self.e2.get()
        self.top.destroy()
        print field + " " +item_search
        matches = self.book.search(item_search,field)
        sub_book = book.Book()
        sub_book.set_entries(matches)
        self.address = sub_book.get_str_entries()
        self.update_list()
#e  how to updating existing values
        # do the search of book here
        # as we have item
        # probably need a display for searched
        #item or place them in first in address book
        # possibly a sort with item in it

    def printPostalE(self):
        first_index = self.list_box.curselection()[0]
        value = self.address[int(first_index)]
#
        entry_to_print = self.to_entry(value)
        index = self.book.get_entry_index(entry_to_print)
        postal = self.book.get_entry(index).to_postal()
        print postal
        self.top = tk.Toplevel(self.parent)
        for line in postal:
            tk.Label(self.top, text=line).pack(padx=20, pady=10)

#
        print "print postal"
        # do the postal rewriting and make it a string
        #self.top = tk.Toplevel(self.parent)
        #tk.Label(self.top, text="Postal line 1").pack(padx=20, pady=10)
        #tk.Label(self.top, text="Postal line 2").pack(padx=20, pady=10)
        #tk.Label(self.top, text="Postal line 3").pack(padx=20, pady=10)

    def sortbyE(self):
        selection_box = PickAttribute(self.parent, self.book)
        """
        self.top = tk.Toplevel(self.parent)
        tk.Label(self.top, text="Field").pack(padx=20, pady=10)
        self.e = tk.Entry(self.top)
        self.e.pack(padx=5)
        b = tk.Button(self.top, text="sort", command=self.sortl)
        b.pack(pady=5)
        print "sortby"
    

    def sortl(self):
        field = self.e.get()
        print field
        self.book.sort(field)
        self.address = self.book.get_str_entries()
        self.update_list()
        self.top.destroy()
        """

    def to_entry(self,value):
        '''
        '''
        attrs = []
        for i in range(len(self.book.get_fields())):
            attrs.append(value.split('\t')[i].split(":")[1])
        return entry.Entry(*attrs)

    def update_list(self):
        '''
        '''
        self.list_box.delete(0,tk.END)
        for item in self.address:
            self.list_box.insert(tk.END, item)
