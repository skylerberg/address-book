import unittest

from address import Book


class TestBook(unittest.TestCase):
    """
    Test the Book class.
    """

    def test_book_initial_size(self):
        book = Book()
        self.assertEquals(len(book), 0)
