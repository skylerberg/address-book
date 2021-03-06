"""
global constants
make it easier to use the name of the attributes of Entry
and the key name in json file(those strings need to follow
variable naming conventions,e.g. no space in between)
"""
LNAME = "Last Name"
FNAME = "First Name"
ADDR = "Address"
CITY = "City"
STATE = "State"
ZIP_CODE = "Zipcode"
PHONE_NUM = "Phone Number"
EMAIL = "Email"

#for actions
NEW = 1
IMPORT = 2
OPEN = 3

#for output on the gui
DELIM = "\t"
#DELIM="|"

#for displaying list
DFNAME = "First name"
DLNAME = "Last name"
DADDR = "Address"
DCITY = "City"
DSTATE = "State"
DZIP_CODE = "Zip code"
DPHONE_NUM = "Phone number"
DEMAIL = "Email"
DLIST = [DFNAME, DLNAME, DADDR, DCITY, DSTATE, DZIP_CODE, DPHONE_NUM, DEMAIL]
DISPLAY_NAMES = {
    FNAME: DFNAME,
    LNAME: DLNAME,
    ADDR: DADDR,
    CITY: DCITY,
    STATE: DSTATE,
    ZIP_CODE: DZIP_CODE,
    PHONE_NUM: DPHONE_NUM,
    EMAIL: DEMAIL}
NON_DISPLAY_NAMES = {
    DFNAME: FNAME,
    DLNAME: LNAME,
    DADDR: ADDR,
    DCITY: CITY,
    DSTATE: STATE,
    DZIP_CODE: ZIP_CODE,
    DPHONE_NUM: PHONE_NUM,
    DEMAIL: EMAIL}
DEFAULTS = {
    FNAME: "John",
    LNAME: "Smith",
    ADDR: "123 Elm Street",
    CITY: "Springfield",
    STATE: "Oregon",
    ZIP_CODE: "12345",
    PHONE_NUM: "(541) 555-0000",
    EMAIL: "John.Smith@example.com"}
