from constants import *


class Entry:
    '''
    A class representing an entry in an address book
    '''

    def __init__(self,
                 fname,
                 lname,
                 addr=None,
                 city=None,
                 state=None,
                 zip_code=None,
                 phone_num=None,
                 email=None,
                 **kwargs):
        '''
        '''
        # kwargs: let user extend the fields
        attr_d = dict()
        attr_d[FNAME] = fname
        attr_d[LNAME] = lname
        attr_d[ADDR] = addr
        attr_d[CITY] = city
        attr_d[STATE] = state
        attr_d[ZIP_CODE] = zip_code
        attr_d[PHONE_NUM] = phone_num
        attr_d[EMAIL] = email

        self.__dict__.update(attr_d)

    def __str__(self):
        return ("firstname:%s\tlastname:%s\taddr:%s\tcity:%s\tstate:%s\tzip:%s\tphone#:%s\temail:%s") \
            % (self.__dict__[FNAME],
               self.__dict__[LNAME],
               self.__dict__[ADDR],
               self.__dict__[CITY],
               self.__dict__[STATE],
               self.__dict__[ZIP_CODE],
               self.__dict__[PHONE_NUM],
               self.__dict__[EMAIL])

    def set_attr(self, attr, value):
        '''
        Edit an attribute in the entry

        :arg attr: The attribute of the entry to be edited
        :arg value: The new value for the target attribute
        :type attr: String
        :type value: String
        '''
        if attr in self.__dict__.keys():
            self.__dict__[attr] = value
        else:
            print "Unimplemented!"
