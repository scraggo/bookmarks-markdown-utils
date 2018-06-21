#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
chr_backup.py
Purpose: backs up the Chrome JSON 'Backup' file and adds date to it.
This file can be run independently.
'''

#Standard library:
import os, sys, shutil

#Local modules:
from . import chr_path

# this import only works if you're in this directory
sys.path.insert(0, '../utils')
import date_append as DA
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
