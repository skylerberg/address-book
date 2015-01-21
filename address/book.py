import json

from entry import Entry
from constants import *


class BookEncoder(json.JSONEncoder):
    '''
    Encode :class:`Book` object into JSON format.
    '''
    def default(self, obj):
        if isinstance(obj, Book):
            return {"entries": [entry.__dict__ for entry in obj.entries]}
        return json.JSONEncoder.default(self, obj)


class Book:
    '''
    Implementation of an address book. 
    '''

    def __init__(self, path=None):  # a distinction between new book and opened book
        '''
        :arg path: Path to the file to be opened.
        :type path: String

        :raises IOError: if the file cannot be read.
        '''
        # self.num_fields  may be needed for supporting customized fileds
        self.entries = []
        if path is not None:
            f = open(path)
            book = json.loads(f.read())
            for entry in book["entries"]:
                fname = entry[FNAME]
                lname = entry[LNAME]
                addr = entry[ADDR]
                city = entry[CITY]
                state = entry[STATE]
                zip_code = entry[ZIP_CODE]
                phone_num = entry[PHONE_NUM]
                email = entry[EMAIL]
                self.entries.append(Entry(fname,
                                          lname,
                                          addr,
                                          city,
                                          state,
                                          zip_code,
                                          phone_num,
                                          email))
            f.close()

    def add_entry(self, entry):
        '''
        Add an entry to the book

        :arg entry: An object of Entry class, representing an entry in an
          address book
        :type entry: Entry
        '''
        self.entries.append(entry)

    def show_entry(self):
        '''
        Print all the entries in the book
        '''
        for index, entry in enumerate(self.entries):
            print index, entry

    def save_as(self, path):
        '''
        Save the book into a file using json format

        :arg path: The path to the file, if the file exists, it will be
          overwritten
        :type path: String
        '''
        f = open(path, "w")
        json.dump(self, f, cls=BookEncoder)
        f.close()

    def sort(self, attr):
        '''
        Sort the entries based on one of the attributes

        :arg attr: The attribute to be based on
        :type attr: String
        '''

        if attr == LNAME:
            self.entries = sorted(self.entries, key=lambda entry: entry.__dict__[LNAME])
        elif attr == FNAME:
            self.entries = sorted(self.entries, key=lambda entry: entry.__dict__[FNAME])
        elif attr == ZIP_CODE:
            self.entries = sorted(self.entries, key=lambda entry: entry.__dict__[ZIP_CODE])
        else:
            print "Unimplemented!"

    def delete_entry(self, index):
        '''
        Delete an entry from the book

        :arg index: The index of the entry to be deleted
        :type index: Int
        '''
        entry = self.entries.pop(index)  # save the deleted entry in case the user wants to withdraw

    def edit_entry(self, index, attr, value):
        '''
        Edit an existing entry in the book

        :arg index: The index of the entry to be edited
        :arg attr: The attribute of the entry to be edited
        :arg value: The new value for the target attribute
        :type index: Int
        :type attr: String
        :type value: String

        '''
        self.entries[index].set_attr(attr, value)

    def __len__(self):
        '''
        Get the number of entries in the book

        :returns: Number of entries in the book
        :rtype: Int
        '''
        return len(self.entries)

    def import_from(self,path):# for now, only the required ones
        '''
        Import address from a tsv file

        :arg path: Path to the file to be imported.
        :type path: String

        :raises IOError: if the file cannot be read.
        '''
        f = open(path)
        for line in f:
            fields = line.rstrip().split("\t")
            city,state,zip_code = fields[0].split("  ")#use 2 spaces(in case city name is two-word, or city/state is missing)
            addr = fields[1] +" " + fields[2]
            fname = fields[3].split("  ")[0]
            lname = fields[3].split("  ")[1]
            phone_num = fields[4]
            email = fields[5]
            self.entries.append(Entry(fname,
                                      lname,
                                      addr,
                                      city,
                                      state,
                                      zip_code,
                                      phone_num,
                                      email
                                      ))
        f.close()

    def export_to(self,indexes, path):
        '''
        Export address to a tsv file

        :arg path: Path of the destination file.
        :arg indexes: Indexes of the entries to be exported
        :type path: String
        :type indexes: List of Int

        :raises IOError: if the file cannot be read.
        '''
        f = open(path,"w")
        for i in indexes:
            entry = self.entries[i]
            last = entry.get_attr(CITY) + "  " + entry.get_attr(STATE) + "  " + entry.get_attr(ZIP_CODE)#use 2 spaces
            delivery = entry.get_attr(ADDR)
            second = ""
            recipient = entry.get_attr(FNAME) + "  " + entry.get_attr(LNAME)#use 2 spaces
            phone = entry.get_attr(PHONE_NUM)
            email = entry.get_attr(EMAIL)
            f.write(("%s\t%s\t%s\t%s\t%s\t%s\n")%(last,delivery,second,recipient,phone,email))
        f.close()

    def merge(self,other):#to be tested
        '''
        Merge two address books, removing duplicated entries, all the entries are merged into the current book

        :arg other: The other book to be merged with the current one
        :type string: Book
        '''
        for entry in other.entries:
            if not entry in self.entries:
                self.add_entry(entry)

    def search(self,string):
        '''
        Search all the entries containing a specific string in the address book 

        :arg string: the string to be searched
        :type string: String

        :returns: A list of entries containing the string
        :rtype: List
        '''
        matches = []
        for entry in self.entries:
            for key in entry.__dict__:
                if (entry.__dict__[key] is not None) and (string.lower() in entry.__dict__[key].lower()):
                    matches.append(entry)
                    break
        return matches
