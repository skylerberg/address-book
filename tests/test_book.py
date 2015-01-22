import unittest

from address import Book


class TestBook(unittest.TestCase):
    """
    Test the Book class.
    """

    def test_book_initial_size(self):
        book = Book()
        self.assertEquals(len(book), 0)

    def test_book_size_with_two_entries(self):
        en1 = Entry("person1")
        en2 = Entry("person2")
        book = Book()
        book.add_entry(en1)
        book.add_entry(en2)
        self.assertEquals(len(book), 2)

    def test_book_delete_one_entry(self):
        en1 = Entry("person1")
        en2 = Entry("person2")
        book = Book()
        book.add_entry(en1)
        book.add_entry(en2)
        book.delete_entry(en1)
        self.assertEquals(len(book), 1)

    def test_book_edit_entry(self):
        en1 = Entry("person1")
        book = Book()
        book.add_entry(en1)
        book.edit_entry(0,FNAME,"William")
        self.assertEquals(entry.get_attr(address.entry.FNAME), "William")

    def test_book_merge_two_books_with_duplicated_entries(self):
        book1 = Book()
        book2 = Book()
        en1 = Entry("Stephanie","Nichols","3018 Annamark Lane")
        en2 = Entry("stephanie","nichols","3018 annamark lane")
        en3 = Entry("Stephanie","Nichols","3018 Annamark Lane")
        en4 = Entry("Thomas","Meyer","3018 Annamark Lane")
        book1.add_entry(en1)
        book1.add_entry(en2)
        book2.add_entry(en3)
        book2.add_entry(en4)
        book1.merge(book2)
        self.assertEquals(len(book1), 3)

    def test_book_search_string_in_three_entries(self):
        book = Book()
        en1 = Entry("Stephanie","Nichols","3018 Annamark Lane")
        en2 = Entry("stephanie","nichols","3018 annamark lane")
        en3 = Entry("Thomas","Meyer","3018 Annamark Lane STE 4")
        book1.add_entry(en1)
        book1.add_entry(en2)
        book1.add_entry(en3)
        ret = book1.search("ste")
        self.assertEquals(len(ret), 3)

