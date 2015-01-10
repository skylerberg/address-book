
import json

class BookEncoder(json.JSONEncoder):
    '''
    Encode :class:`Book` class object into json format
    '''
    def default(self, obj):
        if isinstance(obj, Book):
            return {"entries":[entry.__dict__ for entry in obj.entries]}
        return json.JSONEncoder.default(self, obj)


class Book():
    '''
    First implementation of an address book with very simple functionality.
    For now, it can create new book, open a book, save a book, add entries, and print all the entries.
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
                fname = entry["fname"]
                lname = entry["lname"]
                addr = entry["addr"]
                city = entry["city"]
                state = entry["state"]
                zip_code = entry["zip_code"]
                phone_num = entry["phone_num"]
                email = entry["email"]
                self.entries.append(Entry(fname,lname,addr,city,state,zip_code,phone_num,email))
            f.close()
            
    def add_entry(self,entry):
        '''
        Add an entry to the book

        :arg entry: An object of Entry class, representing an address in an address book
        :type entry: Entry
        '''
        self.entries.append(entry)
    
    def show_entry(self):
        '''
        Print all the entries in the book

        :arg entry: An object of Entry class, representing an address in an address book
        :type entry: Entry
        '''
        for entry in self.entries:
            print entry

    def save_as(self,path):
        '''
        Save the book into a file using json format

        :arg entry: An object of Entry class, representing an address in an address book
        :type entry: Entry
        '''
        f = open(path,"w")
        json.dump(self,f,cls=BookEncoder)
        f.close()

    def delete_entry(self):#to be implemented
        pass


class Entry:
    '''
    A class representing an entry in an address book
    '''
    def __init__(self, fname, lname, addr=None, city=None, state=None, zip_code=None, phone_num=None, email=None):
        '''
        '''
        #todo let user extend the fields
        self.fname = fname
        self.lname = lname
        self.addr = addr
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_num = phone_num
        self.email = email

    def __str__(self):
        return ("firstname:%s  lastname:%s  addr:%s  city:%s  state:%s  zip:%s  phone#:%s  email:%s  ") \
                % (self.fname, self.lname, self.addr, self.city, self.state, self.zip_code, self.phone_num, self.email)


def main():
    while True:
        print "\nSelect an action, then hit enter:\
               \n1-Creat a new book\
               \n2-Open a book\
               \n9-quit"
              
        inp = raw_input()
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
                    \n9-return to up level"
                    
                inp2 = raw_input()
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
