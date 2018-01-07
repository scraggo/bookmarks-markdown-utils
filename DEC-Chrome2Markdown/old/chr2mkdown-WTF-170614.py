#pythontemplate
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 4/26/17, 11:18 AM

@author: davecohen

Title: Convert Chrome Bookmarks JSON file to Markdown

Output Format:
* [UPS: Register](https://www.ups.com/one-to-one/login) - [https://www.ups.com/one-to-one/login](https://www.ups.com/one-to-one/login)

Input Example:
"name": "UPS: Register",
"url": "chrome-extension://klbibkeccnjlkjkiokjodocebajanakg/suspended.html#uri=https://www.ups.com/one-to-one/login"

parsing:
delete: "type": "url",
replace: 
"name": with [ ]
"url": with ( )


"""
#Standard library:
import os, sys, re, shutil
#Local modules:
from chr_config import myConfig
import date_append as DA
from chr_path import getChromePath

def deleter(str):
    str = str\
    .replace('"type": "url",', '')
    return str
    
def replacer(str):
    str = str                       \
    .replace('<a', '</p>\n<a')      \
    .replace('</a>', '</a>\n - ')
    return str

def fileExists(filePath):
    if os.path.exists(filePath):
        raise OSError(filePath + ' file exists.')

###CHECKS
print('''
DON'T FORGET:
    -make sure that your mobile bookmarks have synced to desktop
    -make sure to put the ---MOBILE file at the top of the mobile folder
    -if you feel sure that you're ready, you can delete bookmarks after this backup.
READY? hit Enter.''')
yes = input('')
###

md_oTemp = os.path.join(myConfig['myBackupDest'], myConfig['myMDfile'])
md_output = DA.date_append(md_oTemp)
fileExists(md_output) #raises error if exists

chr_dir, chr_file = os.path.split(getChromePath())
print(chr_dir, chr_file)
sys.exit()