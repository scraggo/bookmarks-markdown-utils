
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
chr_backup.py
Purpose: backs up the Chrome JSON 'Backup' file and adds date to it.
Dependencies:
    chr_config.py
    chr_path.py
    date_append.py
This file can be run independently of chr2mkdown.
'''

#Standard library:
import os, sys, shutil
#Local modules:
from chr_config import directories
import date_append as DA
import chr_path
from file_utils import FileUtils


def chrBackup():
    '''
    copy and rename 'Bookmarks' file with date appended to it to 
    specified directory in config,
    '''
    fileUtils = FileUtils()
    #Get chrome path of Bookmarks file
    chr_fullPath = chr_path.getChromeJSON(chr_path.getChromePath())

    chr_file = os.path.split(chr_fullPath)[1]

    #Append date
    fileWithDate = DA.date_append_filename(chr_file)

    #Return path of copied file - error thrown if exists
    return fileUtils.copy_to_chrJsonBackupsDir(chr_fullPath, fileWithDate)
