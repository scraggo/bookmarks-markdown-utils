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
from chr_config import myConfig
import date_append as DA
from chr_path import *

def fileExists(filePath):
    if os.path.exists(filePath):
        raise OSError(filePath + ' file exists.')

def chrBackup():
    #Chrome file - check output location
    chr_fullPath = getChromeJSON(getChromePath())

    chr_dir, chr_file = os.path.split(chr_fullPath)
    chr_output = os.path.join(myConfig['myBackupDest'], chr_file)
    fileExists(chr_output) #raises error if exists

    shutil.copy(chr_fullPath, myConfig['myBackupDest'])

    chr_rename = DA.date_append(chr_output)
    fileExists(chr_rename) #raises error if exists

    shutil.move(chr_output, chr_rename)