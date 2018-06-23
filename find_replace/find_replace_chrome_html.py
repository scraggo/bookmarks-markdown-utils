#pythontemplate
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 4/26/17, 11:18 AM

@author: davecohen

usage:
'python find_replace_clean_html.py <html file> [<output path>]'

Title: Find / Replace in HTML

Description:
This script finds and replaces or removes certain html tags.
It can be ran after
- exporting a bookmarks.html file from Chrome
- "clearning" html (I used https://html-cleaner.com/)
"""
import os, json, sys

from replacer import replacer
from create_file import create_file

# this import only works if you're in this directory
sys.path.insert(0, '../utils')
from get_config import get_json_config


def get_replaced_line(line):
    '''This function is file-specific
    '''
    to_delete = [
        ['<p></p>', ''],
        ['<p> </p>', ''],
        ['<dd>', ''],
        ['</dd>', '']
    ]
        
    to_replace = [
        ['<dl>', '<ul>'],
        ['</dl>', '</ul>'],
        ['<dt>', '<li>'],
        ['</dt>', '</li>']
    ]
    if line == '':
        return line
    
    replaced = replacer(to_delete + to_replace, line)
    if replaced == '':
        return replaced
    
    return replaced + '\n'

def main():
    html_file = sys.argv[1]

    config = get_json_config()

    user_output_path = sys.argv[2]
    if user_output_path:
        outputlocation = user_output_path
    else:
        output_filename = 'chrome_output.html'
        outputlocation = os.path.join(config['directories']['bookmarksRootDir'], output_filename)

    write_mode = 'w'
    create_file(outputlocation, write_mode, html_file, get_replaced_line)

if __name__ == '__main__':
    main()