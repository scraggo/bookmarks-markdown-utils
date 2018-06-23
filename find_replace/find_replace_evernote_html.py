#pythontemplate
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 4/26/17, 11:18 AM

@author: davecohen

usage:
'python find_replace_clean_html.py <html file>'

Title: Find / Replace in HTML
"""
import os, json, sys

from replacer import replacer
from create_file import create_file
from get_args import get_args

# this import only works if you're in this directory
sys.path.insert(0, '../utils')
from get_config import get_json_config

def get_replaced_line(line):
    '''This function is file-specific
    '''
    to_delete = [
        ['<div> </div>', ''],
        ['<p></p>', ''],
        ['<div>', ''],
        ['</div>', '']
    ]
        
    to_replace = [
        ['<a', '</p>\n<a'],
        ['</a>', '</a>\n - ']
    ]
    if line == '':
        return line
    
    line = line.replace('<div><br/>', '<p>')
    line = replacer(to_delete, line)
    line = line.strip()

    if line == '':
        return line
    
    return replacer(to_replace, line) + '\n'

def main():
    description_str = '''Description:
    This script finds and replaces or removes certain html tags.
    It can be ran after
    - exporting an html file from Evernote
    - "clearning" html (I used https://html-cleaner.com/)'''

    args = get_args(
        description_str,
        {
            "flag": "html_file",
            "help": "evernote html file"
        },
        {
            "flag": "-o",
            "help": "full output file path and name"
        }
        )

    html_file = args.html_file
    output_location = args.o
    if not output_location:
        output_filename = 'evernote_output.html'
        config = get_json_config()
        outputlocation = os.path.join(config['directories']['bookmarksRootDir'], output_filename)

    create_file(outputlocation, 'w', html_file, get_replaced_line)

if __name__ == '__main__':
    main()
