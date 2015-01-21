import unittest

import address.entry


class TestEntry(unittest.TestCase):
    """
    Test the Entry class.
    """

    def test_no_values(self):
        address.entry.Entry()

    def test_get_first_name(self):
        entry = address.entry.Entry("William")
        self.assertEquals(entry.get_attr(address.entry.FNAME), "William")

    def test_get_nonexistant_field(self):
        entry = address.entry.Entry()
        with self.assertRaises(KeyError):
            self.assertEquals(entry.get_attr("undefined"))

    def test_get_unset_mandatory_field(self):
        entry = address.entry.Entry()
        self.assertEquals(entry.get_attr(address.entry.FNAME), None)

    def test_change_field_value(self):
        entry = address.entry.Entry("William")
        self.assertEquals(entry.get_attr(address.entry.FNAME), "William")
        entry.set_attr(address.entry.FNAME, "Bill")
        self.assertEquals(entry.get_attr(address.entry.FNAME), "Bill")

    def test_set_nonexistant_field(self):
        entry = address.entry.Entry()
        with self.assertRaises(KeyError):
            entry.set_attr("undefined", "value")

    def test_compare_different_entries(self):
        entry1 = address.entry.Entry("William","Bill","1 1st street apt 1")
        entry2 = address.entry.Entry("William","Bill","1 1st street apt 2")
        self.assertFalse(entry1 == entry2)

    def test_compare_same_entries(self):
        entry1 = address.entry.Entry("William","Bill","1 1st street apt 1")
        entry2 = address.entry.Entry("William","Bill","1 1st street apt 1")
        self.assertTrue(entry1 == entry2)
