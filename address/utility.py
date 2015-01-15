'''
This module contains some common functions
For now, things are simplified..
'''

import re
from constants import *

def validate(attr,string): #return value may need to be improved
    '''
    Validate if a string matches the format of a specific attribute

    :arg attr: The specific attribute
    :arg string: The string to be validated
    :type attr: String
    :type value: String

    :returns: A corresponding MatchObject instance or True if the string matches. None if it does not match 
    :rtype: Mathcobject or None
    '''
    if attr == EMAIL:
        return re.match(r"^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.\w+$",string)
    elif attr == PHONE_NUM:
        return re.match(r"^\d{9,10}$",string)
    elif attr == ADDR:
        return re.match(r"^\d{1,6}( +\w+){2,3}( +\w{2,4} \d{1,5})?$",string)
    elif attr == ZIP_CODE:
        return re.match(r"^\d{5}$|^\d{5}-\d{4}$",string)
    else:
        return True #if the check is unimplememted, return true for now

def test():
    print validate(EMAIL,"a#b@abc.com")
    print validate(EMAIL,"abcde@gmail.com")
    print validate(ADDR,"123 15th ave apt 11")
    print validate(ADDR,"123 15th ave")
    print validate(ZIP_CODE,"12345")
    print validate(ZIP_CODE,"12345-3456")

if __name__ == "__main__":
    test()