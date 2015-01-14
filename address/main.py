import sys
from book import Book
from entry import Entry
from constants import *
import utility


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
                try:
                    path = raw_input("book path:").strip()
                    b = Book(path)
                except IOError:
                    sys.stderr.write("\nFile '%s' cannot be read!\n"%path)
                    continue
            while True:
                print "\nSelect an action for the book: \
                    \n1-add entry\
                    \n2-print entry\
                    \n3-save as\
                    \n4-sort by(fname, lname or zip_code)\
                    \n5-delete an entry(by index based on print)\
                    \n6-edit an entry\
                    \n9-return to up level"

                inp2 = raw_input().strip()
                if not inp2.isdigit():
                    print "Invalid input!"
                    continue
                choice2 = int(inp2)
                if choice2 == 1:
                    fname = raw_input("firstname:").strip()
                    lname = raw_input("lastname:").strip()
                    b.add_entry(Entry(fname, lname))
                elif choice2 == 2:
                    b.show_entry()
                elif choice2 == 3:
                    path = raw_input("file name:").strip()
                    b.save_as(path)
                elif choice2 == 4:
                    attr = raw_input(("input '%s', '%s' or '%s':") % (FNAME, LNAME, ZIP_CODE)).strip()
                    b.sort(attr)
                elif choice2 == 5:
                    l = b.size()
                    if l == 0:
                        print "Nothing left!"
                        continue
                    index = raw_input("input 0-"+str(l-1)+":").strip()
                    if not index.isdigit() or int(index) < 0 or int(index) > l-1:
                        print "Invalid input!"
                        continue
                    b.delete_entry(int(index))
                elif choice2 == 6:
                    l = b.size()
                    if l == 0:
                        print "Nothing to edit!"
                        continue
                    index = raw_input("select an entry to edit (input 0-"+str(l-1)+"):").strip()
                    if not index.isdigit() or int(index) < 0 or int(index) > l-1:
                        print "Invalid input!"
                        continue
                    attr = raw_input(("select an attribute to edit '%s', '%s', '%s', '%s', '%s', '%s', '%s' or '%s':") % (FNAME, LNAME,ADDR,CITY,STATE,ZIP_CODE,PHONE_NUM,EMAIL)).strip()
                    value = raw_input("input an value for %s:" % attr) .strip()
                    if utility.validate(attr,value):
                        b.edit_entry(int(index),attr,value)
                    else:
                        print ("\nInvalid value for %s!") % attr
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
