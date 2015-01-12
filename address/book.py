import json

from entry import Entry
from constants import *

# global constants
# make it easier to use the name of the attributes of Entry
# and the key name in json file(those strings need to follow
# variable naming conventions,e.g. no space in between)
LNAME = "lname"
FNAME = "fname"
ADDR = "addr"
CITY = "city"
STATE = "state"
ZIP_CODE = "zip_code"
PHONE_NUM = "phone_num"
EMAIL = "email"


class BookEncoder(json.JSONEncoder):
    '''
    Encode :class:`Book` object into json format
    '''
    def default(self, obj):
        if isinstance(obj, Book):
            return {"entries": [entry.__dict__ for entry in obj.entries]}
        return json.JSONEncoder.default(self, obj)


class Book:
    '''
    First implementation of an address book with very simple functionality.
    '''
    def __init__(self, path=None):  # a distinction between new book and opened book
        '''
        :arg path: Path to the file to be opened.
        :type path: String
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
        :arg index: The index of the entry to be deleted
        :type index: Int
        '''
        entry = self.entries.pop(index)  # save the deleted entry in case the user wants to withdraw
