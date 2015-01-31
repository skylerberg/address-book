"""
Displaying warning or error messages to user
"""

import tkMessageBox

ERROR = 0
WARNING = 1
ASK = 2

def message(message_type, message, **kwargs ):
    '''
    Shows error to user, different types of errors, warnings, or asking user.
    args: message types - ERROR, WARNING or ASK
          message - string that is describing the error
          **kwargs - what every is casuing that error. 
    returns : tkMessageBox
    '''
    if message_type == ERROR:
        return tkMessageBox.showerror("Error",message,**kwargs)
    elif message_type == WARNING:
        return tkMessageBox.showwarning("Warning",message,**kwargs)
    elif message_type == ASK:
        return tkMessageBox.askyesno("Wait",message,**kwargs)

