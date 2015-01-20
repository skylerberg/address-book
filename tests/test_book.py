import unittest

from address import Book


class TestTest(unittest.TestCase):
    """
    """

    def test_book_initial_size(self):
        book = Book()
        self.assertEquals(len(book), 0)
