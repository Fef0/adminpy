"""
                \AdminPy/
        Open Windows executable in Python!
    :copyright: (c) 2016 Fef0
    :Thanks to Jorenko from stackoverflow.com for "AsAdmin" function
    :Based on Preston Landers "pyuac" work
    :license: GNU General Public License v3.0
"""
#WARNING: Requires Windows XP SP2 or higher!
import os
import sys
import win32com.shell.shell as shell

def isUserAdmin():
    if os.name == 'nt':
        import ctypes
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            traceback.print_exc()
            return False
    else:
        #Open a Tkinter instance with error if the machine isn't running Windows.
        import Tkinter,tkMessageBox
        root = Tkinter.Tk()
        root.withdraw()
        tkMessageBox.showerror('Error!', 'This tool is for Windows only!')
    
def AsAdmin(arg=None):
    ASADMIN = 'asadmin'
    file2open=arg
    if sys.argv[-1] != ASADMIN:
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
        shell.ShellExecuteEx(lpVerb='runas', lpFile=file2open, lpParameters=params)
