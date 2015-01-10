
import json

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
            return {"entries":[entry.__dict__ for entry in obj.entries]}
        return json.JSONEncoder.default(self, obj)


class Book:
    '''
    First implementation of an address book with very simple functionality.
    '''
    def __init__(self, path = None): #a distinction between new book and opened book
        '''
        :arg path: Path to the file to be opened.
        :type path: String
        '''
        #self.num_fields  may be needed for supporting customized fileds
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
                self.entries.append(Entry(fname,lname,addr,city,state,zip_code,phone_num,email))
            f.close()
            
    def add_entry(self,entry):
        '''
        Add an entry to the book

        :arg entry: An object of Entry class, representing an entry in an address book
        :type entry: Entry
        '''
        self.entries.append(entry)
    
    def show_entry(self):
        '''
        Print all the entries in the book
        '''
        for entry in self.entries:
            print entry

    def save_as(self,path):
        '''
        Save the book into a file using json format

        :arg path: The path to the file, if the file exists, it will be overwritten
        :type path: String
        '''
        f = open(path,"w")
        json.dump(self,f,cls=BookEncoder)
        f.close()

    def sort(self,attr):
        '''
        Sort the entries based on one of the attributes

        :arg attr: The attribute to be based on
        :type attr: String
        '''

        if attr == LNAME:
            self.entries = sorted(self.entries,key=lambda entry:entry.__dict__[LNAME])
        elif attr == FNAME:
            self.entries = sorted(self.entries,key=lambda entry:entry.__dict__[FNAME])
        elif attr == ZIP_CODE:
            self.entries = sorted(self.entries,key=lambda entry:entry.__dict__[ZIP_CODE])
        else:
            print "Unimplemented!"

    def delete_entry(self):#to be implemented
        pass


class Entry:
    '''
    A class representing an entry in an address book
    '''
    def __init__(self, fname, lname, addr=None, city=None, state=None, zip_code=None, phone_num=None, email=None, **kwargs):
        '''
        '''
        #kwargs: let user extend the fields
        attr_d = dict()
        attr_d[FNAME] = fname
        attr_d[LNAME] = lname
        attr_d[ADDR] = addr
        attr_d[CITY] = city
        attr_d[STATE] = state
        attr_d[ZIP_CODE] = zip_code
        attr_d[PHONE_NUM] = phone_num
        attr_d[EMAIL] = email

        self.__dict__.update(attr_d)

    def __str__(self):
        return ("firstname:%s  lastname:%s  addr:%s  city:%s  state:%s  zip:%s  phone#:%s  email:%s  ") \
                % (self.__dict__[FNAME], self.__dict__[LNAME], self.__dict__[ADDR], self.__dict__[CITY], self.__dict__[STATE], self.__dict__[ZIP_CODE], self.__dict__[PHONE_NUM], self.__dict__[EMAIL])


def main():
    while True:
        print "\nSelect an action, then hit enter:\
               \n1-Creat a new book\
               \n2-Open a book\
               \n9-quit"
              
        inp = raw_input().strip()
        if not inp.isdigit():
            print "Invalid input!"
            continue
        choice = int(inp)
        if choice == 1 or choice == 2:
            b = None
            if choice == 1:
                b = Book()
            elif choice == 2:
                path = raw_input("book path:")
                b = Book(path)
            while True:
                print "\nSelect an action for the book: \
                    \n1-add entry\
                    \n2-print entry\
                    \n3-save as\
                    \n4-sort by(fname, lname or zip_code)\
                    \n9-return to up level"
                    
                inp2 = raw_input().strip()
                if not inp2.isdigit():
                    print "Invalid input!"
                    continue
                choice2 = int(inp2)
                if choice2 == 1:
                    fname = raw_input("firstname:")
                    lname = raw_input("lastname:")
                    addr = raw_input("addr:")
                    city =raw_input("city:")
                    state = raw_input("state:")
                    zip_code = raw_input("zip:")
                    phone_num =raw_input("phone number:")
                    email =raw_input("email:")
                    b.add_entry(Entry(fname,lname,addr,city,state,zip_code,phone_num,email))
                elif choice2 == 2:
                    b.show_entry()
                elif choice2 == 3:
                    path = raw_input("file name:")
                    b.save_as(path)
                elif choice2 == 4:
                    attr = raw_input(("input '%s', '%s' or '%s':") % (FNAME,LNAME,ZIP_CODE))
                    b.sort(attr)
                elif choice2 == 9:
                    break
                else:
                    print "Unimplemented!"
        elif choice == 9:
            break
        else:
            print "Unimplemented!"

if __name__ == "__main__":
    main()
