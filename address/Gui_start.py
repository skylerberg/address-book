
from book import *
from entry import *
from Tkinter import *
main_tk_root = [True, ""]
listbox=[]
class StartWindow:

	def __init__(self, parent):
		self.parent = parent
		self.top=self.parent
		self.metadata=["a","aa"]# this is our metadata file
		
		self.name =""
		print self.name
		b = Button(parent, text="new", command=self.new,height=5, width=20)
		b.pack(pady=30)
		b = Button(parent, text="openfile", command=self.openfile,height=5, width=20)
		b.pack(pady=30)
		b = Button(parent, text="import", command=self.importl,height=5, width=20)
		b.pack(pady=30)
		
	def new(self):
                """
                creates a tab to place file name
                calls okay button
                """
		self.top = Toplevel(self.parent)
		Label(self.top, text="FileName").pack()

		self.e = Entry(self.top)
		self.e.pack(padx=5)

		b = Button(self.top, text="okay", command=self.okay)
		b.pack(pady=5)
	
	def importl(self):
                """
                creates a tab to place file path
                calls okay button
                need to fix to have self.path, different from
                file name for import
                """
		print"Need to access file path call our import function"
		self.top = Toplevel(self.parent)
		Label(self.top, text="Filepath/Filename").pack()

		self.e = Entry(self.top)
		self.e.pack(padx=5)
		b = Button(self.top, text="okay", command=self.okay)
		b.pack(pady=5)
		
	def openfile(self):
		"""
                this gets the metadata file name and propertys"""
		if self.name=="":
			print " need to access file from metadata" + self.name
			self.top = Toplevel(self.parent)
                        self.top.grab_set()
                        self.top.bind("<Return>", self._choose)
                        
                        
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

                        
                        
                        buttonFrame = Frame(self.top)
                        buttonFrame.pack(side=BOTTOM)
                        chooseButton = Button(buttonFrame, text="Choose", command=self._choose)
                        chooseButton.pack()
                        cancelButton = Button(buttonFrame, text="Cancel", command=self._cancel)
                        cancelButton.pack(side=RIGHT)
                        
		else:
			print self.name + "a new file or imported file"
                print self.name
		#
		
		# open in main_tk_root[1] addressbook
	def openl(self):
            """
                gets name and can use it to get data file, need to open file
                creates a new window deletes the old
                New window will have file data uploaded on page
            """
           
            root2 = Tk()
            root2.geometry("1500x1250+300+300")    
	    root2.title("Team 2 Address Book")
            main_tk_root[1].destroy()
	    main_tk_root[1] = root2
            main_tk_root[1].update()
	    self.parent =root2
	    
	    d = MainWindow(main_tk_root[1],self.name)
        def _choose(self, event=None):
            """
                Chooses correct file to open"""
            try:
                #
                firstIndex = self.listBox.curselection()[0]
                value = self.metadata[int(firstIndex)]
                self.top.destroy()
                self.name= value
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
class MainWindow:
	def __init__(self, parent,name):
		self.parent = parent
		self.top=self.parent
		self.name=name
		print(name)
		

		# the scroll click bar again here 
		
root = Tk()
root.geometry("500x450+300+300")    
root.title("Team 2 Address Book")
main_tk_root[1] = root
main_tk_root[1].update()

d = StartWindow(main_tk_root[1])

main_tk_root[1].wait_window(d.top)

main_tk_root[1].wait_window()
