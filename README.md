# Adminpy
Tested only in Python 2.7 and Pyinstaller 3.2!
IMPORTANT: In Pyinstaller, remember to delete all "print" function before compile it!

# Example

import adminpy

import sys

def mainfunction():
    print("I'm an Admin!")

def adminrights():
    if not adminpy.isUserAdmin(): #If the program hasn't been opened with admin rights by user,open the UAC(User Account Control)
        try:
         adminpy.AsAdmin(str(sys.argv[0])) #If user allows UAC request, open the same .exe as administrator and close the oldest
            sys.exit(0) #Close the old instance after the opening of the new
        except: #If user doesn't allow UAC request
            print("Users doesn't allow to open it with admin rights")
            return
    else: #If the program has been opened with admin rights by user or by "AsAdmin" function, continue with main function
        mainfunction()
    return

adminrights()
sys.exit(0)
