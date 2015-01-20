import unittest

import address.entry


class TestTest(unittest.TestCase):
    """
    This class is meant to make sure that travis and coveralls are working
    properly.
    """

    def setUp(self):
        pass

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

    def tearDown(self):
        pass
