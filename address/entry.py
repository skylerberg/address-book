from constants import *


class Entry:
    '''
    A class representing an entry in an address book
    '''

    def __init__(self,
                 fname=None,
                 lname=None,
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

    def get_attr(self, attr):
        '''
        Get the value associated with a field name.
        :arg attr: The attribute of the entry to be returned
        :type attr: String

        :returns: The value associated with `attr`.
        :rtype: String

        :raises KeyError: when trying to get a field that does not exist.
        '''
        if attr in self.__dict__:
            return self.__dict__[attr]
        else:
            raise KeyError("No field '{0}' in entry.".format(attr))

    def set_attr(self, attr, value):
        '''
        Edit an attribute in the entry

        :arg attr: The attribute of the entry to be edited
        :arg value: The new value for the target attribute
        :type attr: String
        :type value: String

        :raises KeyError: when trying to set a field that does not exist.
        '''
        if attr in self.__dict__.keys():
            self.__dict__[attr] = value
        else:
            raise KeyError("No field '{0}' in entry.".format(attr))

    def __eq__(self,other):#to be tested
        '''
        Equality test between two entries. Two entries are equal when they have same fields with same values

        :arg other: The other entry to be compared with the current one
        :type other: Entry
        '''
        return self.__dict__ == other.__dict__

    def to_postal(self):
        name = self.__dict__[FNAME] + " " + self.__dict__[LNAME]
        delivery = self.__dict__[ADDR]
        last = self.__dict__[CITY] + " " + self.__dict__[STATE] + " " + self.__dict__[ZIP_CODE]
        phone = self.__dict__[PHONE_NUM]
        return [name,delivery,last,phone]

    #def __hash__(self): may not be needed 
