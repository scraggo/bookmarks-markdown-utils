'''
date_append.py
returns a filepath + today's date in format -yymmdd (example: 170612 for July 12,
    2017.
file can be non-existing, but the directory must be valid.
Example output: /Users/you/test-170612.py
'''
import os
from datetime import datetime as d

def todayDate():
    '''return today's date in format 170612 (yymmdd)
    '''
    return d.now().strftime("%y%m%d")

def date_append(filePath):
    '''param::filePath - a string of a valid filePath for a proposed file to 
    create or overwrite. Example: '/my/valid/directory/proposed-file-name.txt'
    Error thrown if the directory isn't valid.
    Best results if extension is specified properly. Example: '.txt'
    '''
    if os.path.isdir(os.path.dirname(filePath)):
        filename, file_extension = os.path.splitext(filePath)
        return ''.join([filename, '-', todayDate(), file_extension])
    else:
        raise OSError('Directory ' + os.path.dirname(filePath) + ' does not exist.')

#Test
# print(date_append('/Chrome_Bookmarks_backupDEC.py')) #not a file / full path

# print(date_append('/Users/davecohen/Dropbox/Notes/-BookmarkProject/PyBookmarkScripts/DEC-Chrome2Markdown/old')) #is a directory

# print(date_append('/Users/davecohen/Dropbox/Notes/-BookmarkProject/PyBookmarkScripts/DEC-Chrome2Markdown/test.what.py')) #is a valid directory / filename