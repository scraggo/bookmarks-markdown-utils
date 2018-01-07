import os
import platform
import re
import sys
from shutil import copy
import subprocess

# Variable declarations
userhome = os.path.expanduser('~').replace('\\', '\\\\')
useros = platform.system() #checked - Darwin.
destination = os.path.dirname(os.path.realpath(__file__)) #/Users/davecohen/Dropbox/Notes/-BookmarkProject/Chrome-Bookmarks-Parser-master
cmd = ['python', 'Chrome_Bookmarks_MinHTML.py']

def findChrome():

    # Directory references for Chrome pulled from Chromium docs.
    # https://www.chromium.org/user-experience/user-data-directory

    vernum = platform.version()

    # Check if platform is Windows.
    if useros is 'Windows':
        # Determine if OS is XP.
        if re.search('^5\.', vernum):
            profilePath = os.path.normpath(os.path.join(
                userhome, 'Local Settings\\Application Data\\'
                'Google\Chrome\\User Data\\Default'))
            filePath = os.path.normpath(os.path.join(
                profilePath, "Bookmarks.bak"))
            if os.path.exists(filePath):
                copy(filePath, destination)
            else:
                sys.exit("Cannot find Bookmarks.bak file.")

        # Else, assume OS is 10 / 8 / 7 / Vista.
        else:
            profilePath = os.path.normpath(os.path.join(
                userhome, 'AppData\\Local\\Google\\Chrome'
                '\\User Data\\Default'))
            filePath = os.path.normpath(os.path.join(
                profilePath, "Bookmarks.bak"))
            if os.path.exists(filePath):
                copy(filePath, destination)
            else:
                sys.exit("Cannot find Bookmarks.bak file.")

    # Check if platform is Mac OS X.
    elif useros == 'Darwin':
        profilePath = os.path.normpath(os.path.join(
            userhome, 'Library/Application Support/Google/Chrome/Default'))
        filePath = os.path.normpath(os.path.join(
            profilePath, "Bookmarks.bak"))
#         print(filePath) #debug
        if os.path.exists(filePath):
            copy(filePath, destination)
        else:
            sys.exit("Cannot find Bookmarks.bak file.")

    # Check if platform is Linux.
    elif useros is 'Linux':
        profilePath = os.path.normpath(os.path.join(
            userhome, '/.config/google-chrome/Default'))
        filePath = os.path.normpath(os.path.join(
            profilePath, "Bookmarks.bak"))
        if os.path.exists(filePath):
            copy(filePath, destination)
        else:
            sys.exit("Cannot find Bookmarks.bak file.")

# try:
findChrome() #tested and works!
# subprocess.Popen(cmd) #error here...

#/Users/davecohen/Dropbox/Notes/-BookmarkProject/Chrome-Bookmarks-Parser-master/Chrome_Bookmarks_Parser.py
# subprocess.Popen('/Users/davecohen/Dropbox/Notes/-BookmarkProject/Chrome-Bookmarks-Parser-master/Chrome_Bookmarks_MinHTML.py')
subprocess.Popen(cmd)
# except:
#     sys.exit("Oops. Something went wrong.")
print('done') #debug

'''
changed line 49 to ==
changed line 51 to remove the preceding / in Library/etc
'''