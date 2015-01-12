from book import Book
from entry import Entry
from constants import *


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
                    \n5-delete an entry(by index based on print)\
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
                    city = raw_input("city:")
                    state = raw_input("state:")
                    zip_code = raw_input("zip:")
                    phone_num = raw_input("phone number:")
                    email = raw_input("email:")
                    b.add_entry(Entry(fname, lname, addr, city, state, zip_code, phone_num, email))
                elif choice2 == 2:
                    b.show_entry()
                elif choice2 == 3:
                    path = raw_input("file name:")
                    b.save_as(path)
                elif choice2 == 4:
                    attr = raw_input(("input '%s', '%s' or '%s':") % (FNAME, LNAME, ZIP_CODE))
                    b.sort(attr)
                elif choice2 == 5:
                    l = len(b.entries)
                    if l == 0:
                        print "Nothing left!"
                        continue
                    index = raw_input("input 0-"+str(l-1)+":")
                    if not index.isdigit() or int(index) < 0 or int(index) > l-1:
                        print "Invalid input!"
                        continue
                    b.delete_entry(int(index))
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
