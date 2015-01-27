"""
Window for viewing and editing an address book.
"""
import Tkinter as tk
import tkFileDialog
import tkSimpleDialog
import os

from address.constants import *
from address import utility
from address import book
from address import entry


class MainWindow(object):
    """
    Main window class. This window displays the address book and allows the
    user to perform basic CRUD operations.
    """

#
    def __init__(self, parent, name, metadata, action, import_path=None):#since import_path is likely to be different from name..
        if action == NEW:
            self.book = book.Book()
            #print 'here',name,action
        elif action == IMPORT:
            self.book = book.Book()
            self.book.import_from(import_path)
        elif action == OPEN:
            self.book = book.Book(name+SUFFIX)
#
        self.parent = parent
        self.top = self.parent
        self.name = name
        self.value = ""
        self.e2 = ""
        self.elist=[]
        print name
        self.address=self.book.get_str_entries() #["name1, address1, phone1","name2, address2, phone2"]
        self.metadata = metadata
        self.listFields = ["First Name", "Last Name", "Address", "City" ,"State", "Zipcode", "Phone number", "Email"] 
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
        labels = ('Open...', 'New...', 'Save...', 'Save As...', 'Import...',
           'Export...', "Merge...") 
        fmenu.add_command(label=labels[0], command=lambda m=labels[0]: self.openl())
        fmenu.add_command(label=labels[1], command=lambda m=labels[1]: self.newl())
        fmenu.add_command(label=labels[2], command=lambda m=labels[2]: self.savel())
        fmenu.add_command(label=labels[3], command=lambda m=labels[3]: self.saveasl())
        fmenu.add_command(label=labels[4], command=lambda m=labels[4]: self.importl())
        fmenu.add_command(label=labels[5], command=lambda m=labels[5]: self.exportl())
        fmenu.add_command(label=labels[6], command=lambda m=labels[6]: self.mergel())

    def add_tool_menu(self):
        fmenu = tk.Menu(self._menu, name='fmenu')
        self._menu.add_cascade(label='Tools', menu=fmenu, underline=0)
        labels = ('Add entry','Delete entry','Edit entry','Search field','Print postal...','Sort by...','New Field...')
        fmenu.add_command(label=labels[0], command=lambda m=labels[0]: self.addE())
        fmenu.add_command(label=labels[1], command=lambda m=labels[1]: self.deleteE())
        fmenu.add_command(label=labels[2], command=lambda m=labels[2]: self.editE())
        fmenu.add_command(label=labels[3], command=lambda m=labels[3]: self.searchE())
        fmenu.add_command(label=labels[4], command=lambda m=labels[4]: self.printPostalE())
        fmenu.add_command(label=labels[5], command=lambda m=labels[5]: self.sortbyE())
        fmenu.add_command(label=labels[6], command=lambda m=labels[6]: self.newFieldE())
    def newFieldE(self):
        self.top = tk.Toplevel(self.parent)
        tk.Label(self.top, text="New Field").pack(padx=20, pady=10)

        self.e = tk.Entry(self.top)
        self.e.pack(padx=25)

        b = tk.Button(self.top, text="okay", command=self.fieldCheck)
        b.pack(pady=5)
    def fieldCheck(self):
        newfield = self.e.get()
    
        self.top.destroy()
        self.listFields.append(newfield)
        print self.listFields
    def openl(self):
        """
        self.top = Toplevel(self.parent)
        # self.top.grab_set()
        self.top.bind("<Return>", self._choose(self.openf()))
        Label(self.top, text="open file").pack(padx=5, pady=5)
        listFrame = Frame(self.top)
        listFrame.pack(side=TOP, padx=5, pady=5)
        scrollBar = Scrollbar(listFrame)
        scrollBar.pack(side=RIGHT, fill=Y)
        self.listBox = Listbox(listFrame, selectmode=SINGLE)
        self.listBox.pack(side=LEFT, fill=Y)
        scrollBar.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=scrollBar.set)
        self.metadata.sort()

        for item in self.metadata:
                self.listBox.insert(END, item)

        buttonFrame= Frame(self.top)
        buttonFrame.pack(side=BOTTOM)
        chooseButton = Button(buttonFrame, text="Choose", command=self._choose(self.openf()))
        chooseButton.pack()
        cancelButton = Button(buttonFrame, text="Cancel", command=self._cancel)
        cancelButton.pack(side=RIGHT)
        """
        pass

    def openf(self):
        """
        gets name and can use it to get data file, need to open file
        creates a new window deletes the old
        New window will have file data uploaded on page
        """
        root3 = tk.Tk()
        root3.geometry("1500x1250+300+300")
        root3.title("Team 2.1 Address Book")
        #main_tk_root[1].destroy()
        self.top = root3
        if self.action == IMPORT:
            MainWindow(root3,self.name,self.metadata,self.action,self.import_path)
        else:
            MainWindow(root3,self.name,self.metadata,self.action)

    def _choose(self, event=None):
        """
        Chooses correct file to open
        """
        try:
            first_index = self.list_box.curselection()[0]
            value = self.metadata[int(first_index)]
            
            self.top.destroy()
            self.name = value
            event
        except IndexError:
            #print "here"
            self.name = None
            self.top.destroy()

    def _cancel(self, event=None):
        """if not right close and they need to reopen"""
        self.top.destroy()

    def newl(self):
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

        b = tk.Button(self.top, text="okay", command=self.okay)
        b.pack(pady=5)
        print "new"

    def okay(self):
        """
        grabs name for file
        destorys the window
        opens the file
        """
        #if self.e2 != "":
        #    path = self.e2.get()
        #path = ""
#seems okay has to do with new name(new or import)
        self.name = self.e.get()
        if not self.name in self.metadata:
            self.metadata.append(self.name)
        else:
#e what to do
            pass
        self.top.destroy()
        #self.openf(path)
        self.openf()

    def mergel(self):
        #tk.Tk()
        #tk.Label(self.top, text="File1").pack(padx=20, pady=10)
        #check_vars = [(tk.IntVar(self.top)) for i in range(len(self.metadata))]
        #print check_vars
        self.merge_books = {}
        print 'merge metadata',self.metadata
        top = tk.Tk()
        self.top = top
        for i,name in enumerate(self.metadata):
            self.merge_books[name] = tk.IntVar()
            cb = tk.Checkbutton(top, text = name, variable = self.merge_books[name], \
                                     onvalue = 1, offvalue = 0, height=5, \
                                     width = 20)
            cb.pack()
        

        b = tk.Button(top, text="okay", command=self.okayMerge)
        b.pack(pady=5)
        #var1 = tk.IntVar()
        #tk.Checkbutton(self.top, text="male")

        '''
        self.top = tk.Toplevel(self.parent)
        tk.Label(self.top, text="File1").pack(padx=20, pady=10)
        self.e = tk.Entry(self.top)
        self.e.pack(padx=5)
        tk.Label(self.top, text="File2").pack(padx=20, pady=10)
        self.e2 = tk.Entry(self.top)
        self.e2.pack(padx=5)
        b = tk.Button(self.top, text="okay", command=self.okayMerge)
        b.pack(pady=5)
        '''

    def okayMerge(self):
        # open file one and file 2
        # then merger

        for name in self.merge_books:
            #self.merge_books[name] = self.merge_books[name].get()
            print name,self.merge_books[name].get()
        print "merging"
        self.top.destroy()

        top = tk.Tk()
        self.top = top
        self.merge_books_dst = tk.StringVar()
        self.merge_books_name = []
        for i,name in enumerate(self.metadata):
            if self.merge_books[name].get():
                self.merge_books_name.append(name)
                rb = tk.Radiobutton(top, text = name, variable = self.merge_books_dst, \
                                         value = name,\
                                         indicatoron=0,\
                                         height=5, \
                                         width = 20)
                rb.pack()
        

        b = tk.Button(top, text="okay", command=self.okayMerge2)
        b.pack(pady=5)

    def okayMerge2(self):
        '''
        '''
        self.top.destroy()
        name_dst = self.merge_books_dst.get()
        book_dst = book.Book(name_dst+SUFFIX)
        #print book_dst.show_entry()
        for name in self.merge_books_name:
            if name != name_dst:
                b = book.Book(name+SUFFIX)
                book_dst.merge(b)
                self.metadata.remove(name)
#e delete file also
        #print book_dst.show_entry()
        book_dst.save_as(name_dst+SUFFIX)
        utility.store_metadata(self.metadata)
        if name == self.name:
            self.address = book_dst.get_str_entries()
#how to update:
            #self.show()


    def saveasl(self):
        new_name = tkSimpleDialog.askstring("New name for the book", "new name", parent = self.parent)
        if new_name:
            if not new_name in self.metadata:
                self.book.save_as(new_name+SUFFIX)
                self.metadata.append(new_name)
                self.metadata.sort()
                utility.store_metadata(self.metadata)
            else:
#e
                pass


    def savel(self):
#
        self.book.save_as(self.name+SUFFIX)
        if not self.name in self.metadata:
            self.metadata.append(self.name)
            self.metadata.sort()
        utility.store_metadata(self.metadata)
#
        print "open"

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
        for i in range(len(self.listFields)):
            tk.Label(self.top, text=self.listFields[i]).pack(padx=20, pady=10)
            self.elist.append(tk.Entry(self.top))
            self.elist[i].insert(0, self.listFields[i])
            self.elist[i].pack(padx=5)
        b = tk.Button(self.top, text="okay", command=self.getaddEntry)
        b.pack(pady=5)

    def getaddEntry(self):
        var = []
        for i in range(len(self.listFields)):
            var.append(self.elist[i].get())
        #self.address.append(var)
#
        self.book.add_entry(entry.Entry(*var))
        self.address = self.book.get_str_entries()
#
        self.top.destroy()
        self.list_box.insert(tk.END, self.address[-1])
        #self.show()
        self.address.sort()
        self.top.destroy()
        main_tk_root[1].update()

    def deleteE(self):
        first_index = self.list_box.curselection()[0]
        value = self.address[int(first_index)]
#
        attrs = []
        for i in range(len(self.listFields)):
            attrs.append(value.split('\t')[i].split(":")[1])
        entry_to_delete = entry.Entry(*attrs)
        self.book.delete_entry(self.book.get_entry_index(entry_to_delete))
        self.address = self.book.get_str_entries()
#
        print value
        #self.address.pop(int(first_index))
        #self.deleteShow()
        #self.show()
        self.list_box.delete(int(first_index))
        main_tk_root[1].update()
        print self.address

    def editE(self):
        
        first_index = self.list_box.curselection()[0]
        self.value = self.address[int(first_index)]
        self.top = tk.Toplevel(self.parent)
        self.elist= []
        for i in range(len(self.listFields)):
            tk.Label(self.top, text=self.listFields[i]).pack(padx=20, pady=10)
            self.elist.append(tk.Entry(self.top))
##
            self.elist[i].insert(0, self.value.split('\t')[i].split(":")[1])
            self.elist[i].pack(padx=5)
        print self.elist
        self.index = int(first_index)
        b = tk.Button(self.top, text="okay", command=self.getEditEntry)
        b.pack(pady=5)

    def getEditEntry(self):
#
        var = []
        attrs_pre = []
        for i in range(len(self.listFields)):
            var.append(self.elist[i].get())
            attrs_pre.append(self.value.split('\t')[i].split(":")[1])

        
        #delete then add new
        entry_pre = entry.Entry(*attrs_pre)
        entry_new = entry.Entry(*var)
        self.book.delete_entry(self.book.get_entry_index(entry_pre))

        self.book.add_entry(entry_new)
        self.address = self.book.get_str_entries()
#
        #self.address[self.index] = var
        self.top.destroy()
        self.list_box.delete(int(self.index))
        #self.list_box.insert(tk.END, self.address[self.index])
        self.list_box.insert(tk.END, str(entry_new))
        self.address.sort()
        self.top.destroy()
        main_tk_root[1].update()
        print self.address[self.index]

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
#e  how to updating existing values
        # do the search of book here
        # as we have item
        # probably need a display for searched
        #item or place them in first in address book
        # possibly a sort with item in it
        main_tk_root[1].update()

    def printPostalE(self):
        first_index = self.list_box.curselection()[0]
        value = self.address[int(first_index)]
#
        attrs = []
        for i in range(len(self.listFields)):
            attrs.append(value.split('\t')[i].split(":")[1])
        entry_to_print = entry.Entry(*attrs)
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
        self.top = tk.Toplevel(self.parent)
        tk.Label(self.top, text="Field").pack(padx=20, pady=10)
        self.e = tk.Entry(self.top)
        self.e.pack(padx=5)
        b = tk.Button(self.top, text="sort", command=self.sortl)
        b.pack(pady=5)
        print "sortby"
    

    def sortl(self):
        field = self.e.get()
        # do you sorting
        print field
#e
        self.book.sort(field)
        self.address = self.book.get_str_entries()
#
        self.top.destroy()
        main_tk_root[1].update()
