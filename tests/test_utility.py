import unittest

from address import utility


class TestValidate(unittest.TestCase):
    """
    """

    def test_valid_email(self):
        assert(utility.validate(utility.EMAIL, "abcde@gmail.com"))

    def test_invalid_email_pound_sign(self):
        self.assertEquals(utility.validate(utility.EMAIL, "a#b@abc.com"), None)

    def test_invalid_email_missing_at_sign(self):
        self.assertEquals(utility.validate(utility.EMAIL, "abc.com"), None)

    def test_invalid_email_missing_dot(self):
        self.assertEquals(utility.validate(utility.EMAIL, "abc@com"), None)

    def test_valid_address(self):
        assert(utility.validate(utility.ADDR, "123 15th ave"))

    def test_valid_address_with_apt_number(self):
        assert(utility.validate(utility.ADDR, "123 15th ave apt 11"))

    def test_valid_zip(self):
        assert(utility.validate(utility.ZIP_CODE, "12345"))

    def test_invalid_zip(self):
        self.assertEquals(utility.validate(utility.ZIP_CODE, "1234"), None)

    def test_valid_zip_plus_4(self):
        assert(utility.validate(utility.ZIP_CODE, "12345-3456"))

    def test_invalid_zip_plus_4(self):
        self.assertEquals(utility.validate(utility.ZIP_CODE, "12345-34567"),
                          None)

    def test_has_invalid_field(self):
        self.assertEquals(utility.has_invalid_field("1 abc st","12345","1234567890","bademail"),"Email")
