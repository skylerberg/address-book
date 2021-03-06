import unittest

from address import Book
import address.entry



class TestBook(unittest.TestCase):
    """
    Test the Book class.
    """

    def test_book_initial_size(self):
        book = Book()
        self.assertEquals(len(book), 0)

    def test_book_size_with_two_entries(self):
        en1 = address.entry.Entry("person1")
        en2 = address.entry.Entry("person2")
        book = Book()
        book.add_entry(en1)
        book.add_entry(en2)
        self.assertEquals(len(book), 2)

    def test_book_delete_one_entry(self):
        en1 = address.entry.Entry("person1")
        en2 = address.entry.Entry("person2")
        book = Book()
        book.add_entry(en1)
        book.add_entry(en2)
        book.delete_entry(0)
        self.assertEquals(len(book), 1)

    def test_book_edit_entry(self):
        en1 = address.entry.Entry("person1")
        book = Book()
        book.add_entry(en1)
        book.edit_entry(0,address.entry.FNAME,"William")
        self.assertEquals(book.get_entry(0).get_attr(address.entry.FNAME), "William")

    def test_book_merge_two_books_with_duplicated_entries(self):
        book1 = Book()
        book2 = Book()
        en1 = address.entry.Entry("Stephanie","Nichols","3018 Annamark Lane")
        en2 = address.entry.Entry("stephanie","nichols","3018 annamark lane")
        en3 = address.entry.Entry("Stephanie","Nichols","3018 Annamark Lane")
        en4 = address.entry.Entry("Thomas","Meyer","3018 Annamark Lane")
        book1.add_entry(en1)
        book1.add_entry(en2)
        book2.add_entry(en3)
        book2.add_entry(en4)
        book1.merge(book2)
        self.assertEquals(len(book1), 3)

    def test_book_search_string_in_three_entries(self):
        book = Book()
        en1 = address.entry.Entry("Stephanie","Nichols","3018 Annamark Lane")
        en2 = address.entry.Entry("stephanie","nichols","3018 annamark lane")
        en3 = address.entry.Entry("Thomas","Meyer","3018 Annamark Lane STE 4")
        book.add_entry(en1)
        book.add_entry(en2)
        book.add_entry(en3)
        ret = book.search("ste")
        self.assertEquals(len(ret), 3)

    def test_book_search_string_in_three_entries_with_field(self):
        book = Book()
        en1 = address.entry.Entry("Stephanie","Nichols","3018 Annamark Lane")
        en2 = address.entry.Entry("stephanie","nichols","3018 annamark lane")
        en3 = address.entry.Entry("Thomas","Meyer","3018 Annamark Lane STE 4")
        book.add_entry(en1)
        book.add_entry(en2)
        book.add_entry(en3)
        ret = book.search("ste","Address")
        self.assertEquals(len(ret), 1)

    def test_book_sort_with_two_entries(self):
        en1 = address.entry.Entry("fnamea","lnameb")
        en2 = address.entry.Entry("fnameb","lnamea")
        book1 = Book()
        book2 = Book()
        book1.add_entry(en1)
        book1.add_entry(en2)
        book2.add_entry(en2)
        book2.add_entry(en1)
        book1.sort("First Name")
        book2.sort("First Name")
        self.assertEquals(book1.get_entry(0), book2.get_entry(0))

    def test_book_get_index_of_entry(self):
        book = Book()
        en1 = address.entry.Entry("Stephanie","Nichols","3018 Annamark Lane")
        en2 = address.entry.Entry("stephanie","nichols","3018 annamark lane")
        en3 = address.entry.Entry("Thomas","Meyer","3018 Annamark Lane STE 4")
        book.add_entry(en1)
        book.add_entry(en2)
        book.add_entry(en3)
        en = address.entry.Entry("Stephanie","Nichols","3018 Annamark Lane")
        index = book.get_entry_index(en)
        self.assertEquals(index, 0)

    def test_book_set_entries(self):
        book = Book()
        en1 = address.entry.Entry("Stephanie","Nichols","3018 Annamark Lane")
        en2 = address.entry.Entry("stephanie","nichols","3018 annamark lane")
        en3 = address.entry.Entry("Thomas","Meyer","3018 Annamark Lane STE 4")
        ens = [en1,en2,en3]
        book.set_entries(ens)
        self.assertEquals(len(book), 3)

    def test_book_add_field(self):
        book = Book()
        en1 = address.entry.Entry("Stephanie","Nichols","3018 Annamark Lane")
        book.add_field("new_field")
        self.assertEquals(len(book.get_fields()), 9)
