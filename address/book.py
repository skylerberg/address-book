import json
import csv

from entry import Entry
from constants import *


class BookEncoder(json.JSONEncoder):
    '''
    Encode :class:`Book` object into JSON format.
    '''
    def default(self, obj):
        if isinstance(obj, Book):
            return {"entries": [entry.__dict__ for entry in obj.entries],
                    "fields": obj.fields}
        return json.JSONEncoder.default(self, obj)


class Book(object):
    '''
    Implementation of an address book. 
    '''

    def __init__(self, path=None):  # a distinction between new book and opened book
        '''
        :arg path: Path to the file to be opened.
        :type path: String
        '''
        # self.num_fields  may be needed for supporting customized fileds
        self.entries = []
        self.fields = [LNAME,
                       FNAME,
                       ADDR,
                       CITY,
                       STATE,
                       ZIP_CODE,
                       PHONE_NUM,
                       EMAIL]
        if path is not None:
            f = open(path)
            book = json.loads(f.read())
            for entry in book.get("entries", {}):
                self.entries.append(Entry(**entry))
            self.fields = book.get("fields", self.fields)
            f.close()
        for entry in self.entries:
            for field in self.fields:
                if field not in entry.__dict__:
                    entry.__dict__[field] = ""

    def add_entry(self, entry):
        '''
        Add an entry to the book

        :arg entry: An object of Entry class, representing an entry in an
          address book
        :type entry: Entry
        '''
        if entry not in self.entries:
            self.entries.append(entry)
        else:
#e should raise exception:
            pass

    def show_entry(self):
        '''
        Print all the entries in the book
        '''
        for index, entry in enumerate(self.entries):
            print index, entry

    def sort(self, attr):
        '''
        Sort the entries based on one of the attributes

        :arg attr: The attribute to be based on
        :type attr: String
        '''
        if attr in self.fields:
            self.entries = sorted(self.entries, key=lambda entry: entry.__dict__[attr])
        else:
            print "No such field this book."

    def delete_entry(self, index):
        '''
        Delete an entry from the book

        :arg index: The index of the entry to be deleted
        :type index: Int
        '''
        entry = self.entries.pop(index)  # save the deleted entry in case the user wants to withdraw

    def get_entry(self,index):
        '''
        Return an entry from the book based on index

        :arg index: The index of the entry to be returned
        :type index: Int

        :returns: An entry in the book
        :rtype: Entry
        '''
        return self.entries[index]

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

    def import_from(self,path):
        '''
        Import address from a tsv file

        :arg path: Path to the file to be imported.
        :type path: String
        '''
        f = open(path)
        reader = csv.reader(f,delimiter="\t")
        for row in reader:
            #assert(len(row) == 5)#assumption of the input format, without email
            #assert(len(row) == 6)#assumption of the input format, with email
            city,state,zip_code = row[0].split("  ")#use 2 spaces(in case city name is two-word, or city/state is missing)
            addr = row[1] +" " + row[2]
            fname = row[3].split("  ")[0]
            lname = row[3].split("  ")[1]
            phone_num = row[4]
            email = row[5]
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
        '''
        f = open(path,"w")
        writer = csv.writer(f,delimiter="\t")
        for i in indexes:
            entry = self.entries[i]
            city = entry.get_attr(CITY) or ''
            state = entry.get_attr(STATE) or ''
            zip_code = entry.get_attr(ZIP_CODE) or ''
            last = city + "  " + state + "  " + zip_code#use 2 spaces
            delivery = entry.get_attr(ADDR)
            second = ""
            fname = entry.get_attr(FNAME) or ''
            lname = entry.get_attr(LNAME) or ''
            recipient = fname + "  " + lname#use 2 spaces
            phone = entry.get_attr(PHONE_NUM)
            email = entry.get_attr(EMAIL) or ''
            #writer.writerow([last,delivery,second,recipient,phone])
            writer.writerow([last,delivery,second,recipient,phone,email])
        f.close()

    def merge(self,other):
        '''
        Merge two address books, removing duplicated entries, all the entries are merged into the current book

        :arg other: The other book to be merged with the current one
        :type other: Book
        '''
        for entry in other.entries:
            if not entry in self.entries:
                self.add_entry(entry)

    def search(self,string,field=None):
        '''
        Search all the entries containing a specific string in the address book 

        :arg string: the string to be searched
        :type string: String

        :returns: A list of entries containing the string
        :rtype: List

        '''
        matches = []
        if not field:
            for entry in self.entries:
                for key in entry.__dict__:
                    if (entry.get_attr(key) is not None) and (string.lower() in entry.get_attr(key).lower()):
                        matches.append(entry)
                        break
            return matches
        else:
            for entry in self.entries:
                if (string.lower() in entry.get_attr(field).lower()):
                    matches.append(entry)
            return matches

    def get_str_entries(self):
        '''
        Get a list of string representation of all the entries in the book. 
        This is used for displaying entries in the gui.
        '''
        ret = []
        for entry in self.entries:
            ret.append(str(entry))
            #ret.append(entry.gui_str())
        return ret

    def get_entry_index(self,entry):
        '''
        Get the index of an entry in the book.

        :arg entry: The entry object to be located
        :type entry: Entry

        :returns: The index of the entry
        :rtype: Int
        '''
        return self.entries.index(entry)

    def set_entries(self,entries):
        '''
        Replace the current list of entries in the book with a new one.

        :arg entries: The new list of entries
        :type entries: List

        '''
        self.entries = entries

    def add_field(self, field):
        '''
        '''
        if field not in self.fields:
            self.fields.append(field)
            for entry in self.entries:
                entry.__dict__[field] = entry.__dict__.get(field, "")

    def get_fields(self):
        return self.fields
