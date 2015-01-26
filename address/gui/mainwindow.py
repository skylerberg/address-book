"""
Window for viewing and editing an address book.
"""
import Tkinter as tk

from address.constants import main_tk_root


class MainWindow(object):
    """
    Main window class. This window displays the address book and allows the
    user to perform basic CRUD operations.
    """

    def __init__(self, parent, name, metadata):
        self.parent = parent
        self.top = self.parent
        self.name = name
        self.value = ""
        self.e2 = "" 
        print name
        self.address = ["name1, address1, phone1", "name2, address2, phone2"]
        self.metadata = metadata
        #self.top = Toplevel(self.parent)
        self._menu = tk.Menu(self.parent, name='menu')
        self.build_submenus()
        self.top.config(menu=self._menu)
        #self.top.grab_set() self.show() def show(self):
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
        labels = ('Add entry',
                  'Delete entry',
                  'Edit entry',
                  'Search field',
                  'Print postal...',
                  "Sort by...")
        fmenu.add_command(label=labels[0], command=lambda m=labels[0]: self.addE())
        fmenu.add_command(label=labels[1], command=lambda m=labels[1]: self.deleteE())
        fmenu.add_command(label=labels[2], command=lambda m=labels[2]: self.editE())
        fmenu.add_command(label=labels[3], command=lambda m=labels[3]: self.searchE())
        fmenu.add_command(label=labels[4], command=lambda m=labels[4]: self.printPostalE())
        fmenu.add_command(label=labels[5], command=lambda m=labels[5]: self.sortbyE())

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

    def openf(self, path):
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
        MainWindow(root3, self.name, self.metadata)

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
        if self.e2 != "":
            path = self.e2.get()
        path = ""
        self.name = self.e.get()
        self.top.destroy()
        self.openf(path)

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

        self.top.destroy()
        print "merging"

    def saveasl(self):
        print "open"

    def save(self):
        print "open"

    def importl(self):
        """
        creates a tab to place file path
        calls okay button
        need to fix to have self.path, different from
        file name for import
        """
        self.top = tk.Toplevel(self.parent)
        tk.Label(self.top, text="File Path").pack(padx=20, pady=10)
        self.e = tk.Entry(self.top)
        self.e.pack(padx=5)
        tk.Label(self.top, text="FileName").pack(padx=20, pady=10)
        self.e2 = tk.Entry(self.top)
        self.e2.pack(padx=5)
        b = tk.Button(self.top, text="okay", command=self.okay)
        b.pack(pady=5)

    def exportl(self):
        self.top = tk.Toplevel(self.parent)
        tk.Label(self.top, text="File Path").pack(padx=20, pady=10)
        self.e = tk.Entry(self.top)

        self.e.pack(padx=5)
        tk.Label(self.top, text="FileName").pack(padx=20, pady=10)
        self.e2 = tk.Entry(self.top)
        self.e2.pack(padx=5)
        b = tk.Button(self.top, text="okay", command=self.exportfile)
        b.pack(pady=5)

    def exportfile(self):
        print "exporting"
        self.top.destroy()

    def addE(self):
        print "add"
        self.top = tk.Toplevel(self.parent)

        tk.Label(self.top, text="First Name").pack(padx=20, pady=10)
        self.e = tk.Entry(self.top)
        self.e.insert(0, "firstname")
        self.e.pack(padx=5)
        tk.Label(self.top, text="Last Name").pack(padx=20, pady=10)
        self.e2 = tk.Entry(self.top)
        self.e2.insert(0, "Last")
        self.e2.pack(padx=5)
        tk.Label(self.top, text="Address").pack(padx=20, pady=10)
        self.e3 = tk.Entry(self.top)
        self.e3.insert(0, "Address")
        self.e3.pack(padx=5)
        tk.Label(self.top, text=" City").pack(padx=20, pady=10)
        self.e4 = tk.Entry(self.top)
        self.e4.insert(0, "City")
        self.e4.pack(padx=5)
        tk.Label(self.top, text="State").pack(padx=20, pady=10)
        self.e5 = tk.Entry(self.top)
        self.e5.insert(0, "State")
        self.e5.pack(padx=5)
        tk.Label(self.top, text="Zipcode").pack(padx=20, pady=10)
        self.e6 = tk.Entry(self.top)
        self.e6.insert(0, "Zipcode")
        self.e6.pack(padx=5)
        tk.Label(self.top, text="PhoneNumber").pack(padx=20, pady=10)
        self.e7 = tk.Entry(self.top)
        self.e7.insert(0, "PhoneNumber")
        self.e7.pack(padx=5)
        tk.Label(self.top, text="Email").pack(padx=20, pady=10)
        self.e8 = tk.Entry(self.top)
        self.e8.insert(0, "Email")
        self.e8.pack(padx=5)

        b = tk.Button(self.top, text="okay", command=self.getaddEntry)
        b.pack(pady=5)

    def getaddEntry(self):
        first = self.e.get()
        last = self.e2.get()
        address = self.e3.get()
        city = self.e4.get()
        state = self.e5.get()
        zipcode = self.e6.get()
        Phonenumber = self.e7.get()
        email = self.e8.get()
        self.address.append(first + last+address+city)
        self.top.destroy()
        self.list_box.insert(tk.END, self.address[-1])
        self.address.sort()
        main_tk_root[1].update()

    def deleteE(self):
        first_index = self.list_box.curselection()[0]
        value = self.address[int(first_index)]
        print value
        self.address.pop(int(first_index))
        #self.deleteShow()
        #self.show()
        self.list_box.delete(int(first_index))
        main_tk_root[1].update()
        print self.address

    def editE(self):
        first_index = self.list_box.curselection()[0]
        self.value = self.address[int(first_index)]
        self.top = tk.Toplevel(self.parent)

        tk.Label(self.top, text=" First Name ").pack(padx=20, pady=10)
        self.e = tk.Entry(self.top)
        self.e.insert(0, "firstname")
        self.e.pack(padx=5)
        tk.Label(self.top, text="Last Name").pack(padx=20, pady=10)
        self.e2 = tk.Entry(self.top)
        self.e2.insert(0, "Last")
        self.e2.pack(padx=5)
        tk.Label(self.top, text="Address").pack(padx=20, pady=10)
        self.e3 = tk.Entry(self.top)
        self.e3.insert(0, "Address")
        self.e3.pack(padx=5)
        tk.Label(self.top, text=" City").pack(padx=20, pady=10)
        self.e4 = tk.Entry(self.top)
        self.e4.insert(0, "City")
        self.e4.pack(padx=5)
        tk.Label(self.top, text="State").pack(padx=20, pady=10)
        self.e5 = tk.Entry(self.top)
        self.e5.insert(0, "State")
        self.e5.pack(padx=5)
        tk.Label(self.top, text="Zipcode").pack(padx=20, pady=10)
        self.e6 = tk.Entry(self.top)
        self.e6.insert(0, "Zipcode")
        self.e6.pack(padx=5)
        tk.Label(self.top, text="PhoneNumber").pack(padx=20, pady=10)
        self.e7 = tk.Entry(self.top)
        self.e7.insert(0, "PhoneNumber")
        self.e7.pack(padx=5)
        tk.Label(self.top, text="Email").pack(padx=20, pady=10)
        self.e8 = tk.Entry(self.top)
        self.e8.insert(0, "Email")
        self.e8.pack(padx=5)
        self.index = int(first_index)
        print "edit"
        b = tk.Button(self.top, text="okay", command=self.getEditEntry)
        b.pack(pady=5)

    def getEditEntry(self):
        first = self.e.get()
        last = self.e2.get()
        address = self.e3.get()
        city = self.e4.get()
        state = self.e5.get()
        zipcode = self.e6.get()
        Phonenumber = self.e7.get()
        email = self.e8.get()
        self.address[self.index] = first + last+address+city
        self.top.destroy()
        self.list_box.delete(int(self.index))
        self.list_box.insert(tk.END, self.address[self.index])
        self.address.sort()
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
        # do the search of book here
        # as we have item
        # probably need a display for searched
        #item or place them in first in address book
        # possibly a sort with item in it
        main_tk_root[1].update()

    def printPostalE(self):
        first_index = self.list_box.curselection()[0]
        value = self.address[int(first_index)]
        print "print postal"
        # do the postal rewriting and make it a string
        self.top = tk.Toplevel(self.parent)
        tk.Label(self.top, text="Postal line 1").pack(padx=20, pady=10)
        tk.Label(self.top, text="Postal line 2").pack(padx=20, pady=10)
        tk.Label(self.top, text="Postal line 3").pack(padx=20, pady=10)

    def sortbyE(self):
        self.top = tk.Toplevel(self.parent)
        tk.Label(self.top, text="Field").pack(padx=20, pady=10)
        self.e = tk.Entry(self.top)
        self.e.pack(padx=5)
        b = tk.Button(self.top, text="sort", command=self.sortl)
        b.pack(pady=5)
        print "sortby"
        print self.e.get()

    def sortl(self):
        field = self.e.get()
        # do you sorting
        print field
        self.top.destroy()
        main_tk_root[1].update()
