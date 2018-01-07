#chr2mkdown.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 4/26/17, 11:18 AM

@author: davecohen

Title: Convert Chrome Bookmarks JSON file to Markdown
    and backup Chrome Bookmarks

Dependencies:
    chr_backup.py
    chr_config.py
    chr_path.py
    date_append.py

Output Format:
* [UPS: Register](https://www.ups.com/one-to-one/login) | [https://www.ups.com/one-to-one/login](https://www.ups.com/one-to-one/login)

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
from chr_backup import *
from chr_path import *

def deleter(f_str):
    '''deletes type, url in f_str
    '''
    return f_str\
    .replace('"type": "url",', '')
    
def replacer(f_str):
    '''replaces html <a> tags
    '''
    return f_str                       \
    .replace('<a', '</p>\n<a')      \
    .replace('</a>', '</a>\n - ')



###CHECKS
print('''
DON'T FORGET:
    -make sure that your mobile bookmarks have synced to desktop
    -if you feel sure that you're ready, you can delete bookmarks after this backup.
READY? hit Enter.''')
yes = input('')
###

#Backup bookmarks
chrBackup()

#Markdown file - check output location
md_oTemp = os.path.join(myConfig['myBackupDest'], myConfig['myMDfile'])
md_output = DA.date_append(md_oTemp)
fileExists(md_output) #raises error if exists

# chrJSON = input('')
# chrJSON = '/Users/davecohen/Library/Application Support/Google/Chrome/Default/Bookmarks'

#Create Markdown from original "Bookmarks" file
chrJSON = getChromeJSON(getChromePath())

output = open(md_output, 'w')

with open(chrJSON) as f:
    for line in f:
        line = line.strip()
        line = deleter(line)
        if line.startswith('"name"'):
            line = line.replace('"name": "', '* [')
            line = line.replace('",', ']')
            output.write(line)
        elif line.startswith('"url"'):
            # if 'chrome-extension://' in line:
                # line = re.sub(r"chrome-extension://([a-z])+/suspended.html#uri=", "", line)
            line = re.sub(r"(chrome-extension://)(.+)(uri=)", "", line)
            line = line.replace('"url": "', '(')
            line_paren = line.replace('"', ')')
            line = line_paren + ' | ' + line_paren.replace('(', '[').replace(')', ']') + line_paren
#             print(replacer(line))
            output.write(line + '\n')
        elif line == '"synced": {':
            output.write('\n\n## MOBILE BOOKMARKS\n\n')

output.close()

print('Output to:', md_output, '\n')

# print('done') #debug
