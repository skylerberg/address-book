'''
This module contains some common functions
For now, things are simplified..
'''

import re
from address.constants import *


def has_invalid_field(addr, zip_code, phone_num, email):
    '''
    Validates the format of four attributes: address, zip code, phone number,
    and email. Return a string indicating the invalid field; return None if all
    of them are valid.

    :arg addr: Address
    :type addr: String
    :arg zip_code: Address
    :type zip_code: String
    :arg phone_num: Address
    :type phone_num: String
    :arg email: Address
    :type email: String

    :returns: A string indicating an invalid field.
    :rtype: String
    '''
    if not validate(ADDR, addr):
        return ADDR
    if not validate(ZIP_CODE, zip_code):
        return ZIP_CODE
    if not validate(PHONE_NUM, phone_num):
        return PHONE_NUM
    if not validate(EMAIL, email):
        return EMAIL
    return None


def validate(attr, string):  # return value may need to be improved
    '''
    Validate if a string matches the format of a specific attribute.

    :arg attr: The specific attribute
    :arg string: The string to be validated
    :type attr: String
    :type value: String

    :returns: A corresponding MatchObject instance or True if the string
      matches. None if it does not match.
    :rtype: MatchObject, True, or None
    '''
    if attr == EMAIL:
        return re.match(r"^\s*$|^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.\w+$", string)
    elif attr == PHONE_NUM:
        return re.match(r"^\s*$|^\d{10}$|^\d{7}$|^\d{3}-\d{3}-\d{4}$|^\(\d{3}\) \d{3}-\d{4}$|^\(\d{3}\)\d{3}-\d{4}$|^\d{3}-\d{4}$", string)
    elif attr == ADDR:
        return re.match(r"^\s*$|^\d{1,6}( +\w+){2,3}( +\w{2,4} \d{1,5})?$", string)
    elif attr == ZIP_CODE:
        return re.match(r"^\s*$|^\d{5}$|^\d{5}-\d{4}$", string)
    else:
        return True  # if the check is unimplememted, return true for now
