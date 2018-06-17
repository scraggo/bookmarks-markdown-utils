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
import chr_config as config
import date_append as DA
from file_utils import FileUtils
from chr_path import getChromeJSON

fileUtils = FileUtils()

class MarkdownCreator:
    def __init__(self):
        self.md_output = ''

    def deleter(self, f_str):
        '''deletes type, url in f_str
        '''
        return f_str\
        .replace('"type": "url",', '')
        
    def replacer(self, f_str):
        '''replaces html <a> tags
        '''
        return f_str \
        .replace('<a', '</p>\n<a') \
        .replace('</a>', '</a>\n - ')

    def get_confirmation(self):
        ###CHECKS
        print('''
        DON'T FORGET:
            -make sure that your mobile bookmarks have synced to desktop
            -if you feel sure that you're ready, you can delete bookmarks after this backup.
        READY? hit Enter.
        Not ready? Type any key then Enter to exit.''')
        yes = input('')
        if yes != '':
            return False
        return True

    def create_output_path(self):
        md_oTemp = os.path.join(config.directories['bookmarksRootDir'], config.filenames['chr_md_file_prefix'])
        self.md_output = DA.date_append(md_oTemp)

    def write_bookmarks_to_file(self, _chrJSON):
        output = open(self.md_output, 'w')

        with open(_chrJSON) as f:
            for line in f:
                line = line.strip()
                line = self.deleter(line)
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
        #             print(self.replacer(line))
                    output.write(line + '\n')
                elif line == '"synced": {':
                    output.write('\n\n## MOBILE BOOKMARKS\n\n')

        output.close()

        print('Output to:', self.md_output, '\n')

    def run_script(self):
        if not self.get_confirmation():
            print('Exiting.')
            return

        self.create_output_path()

        #Markdown file - check output location
        fileUtils.fileExists(self.md_output) #raises error if exists

        # chrJSON = input('')
        # chrJSON = '/Users/davecohen/Library/Application Support/Google/Chrome/Default/Bookmarks'

        #Create Markdown from original "Bookmarks" file
        chrJSON = getChromeJSON()

        print('chrJSON', chrJSON)#debug

        self.write_bookmarks_to_file(chrJSON)

        # print('done') #debug
