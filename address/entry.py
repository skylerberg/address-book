from constants import *


class Entry:
    '''
    A class representing an entry in an address book
    '''

    def __init__(self,
                 fname='',
                 lname='',
                 addr='',
                 city='',
                 state='',
                 zip_code='',
                 phone_num='',
                 email='',
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
        self.__dict__.update(kwargs)

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
        '''
        Generates a postal address which conforms usps postal format.
        The result is a list of strings, and each string represents one line in postal address.

        :returns: A list of strings
        :rtype: List
        '''
        name = self.__dict__[FNAME] + " " + self.__dict__[LNAME]
        delivery = self.__dict__[ADDR]
        last = self.__dict__[CITY] + " " + self.__dict__[STATE] + " " + self.__dict__[ZIP_CODE]
        phone = self.__dict__[PHONE_NUM]
        return [name,delivery,last,phone]

    def gui_str(self):
        '''
        '''
        #TODO: display entries in the gui
        ret = ''
        if self.__dict__[FNAME]:
            ret += ("firstname:"+self.__dict__[FNAME]+"\t")
        if self.__dict__[LNAME]:
            ret += ("lastname:"+self.__dict__[LNAME]+"\t")
        if self.__dict__[ADDR]:
            ret += ("address:" + self.__dict__[ADDR]+"\t")
        if self.__dict__[CITY]:
            ret += ("city:" + self.__dict__[CITY]+"\t")
        if self.__dict__[STATE]:
            ret += ("state:"+self.__dict__[STATE]+"\t")
        if self.__dict__[ZIP_CODE]:
            ret += ("zip:"+self.__dict__[ZIP_CODE]+"\t")
        if self.__dict__[PHONE_NUM]:
            ret += ("phone#:"+self.__dict__[PHONE_NUM]+"\t")
        if self.__dict__[EMAIL]:
            ret += ("email:" + self.__dict__[EMAIL]+"\t")
        return ret.rstrip()
    #def __hash__(self): may not be needed 
