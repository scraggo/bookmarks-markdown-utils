#pythontemplate
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 4/26/17, 11:18 AM

@author: davecohen

usage:
'python find_replace_clean_html.py <html file> [<output path>]'

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
    description_str = '''This script finds and replaces or removes certain html tags.
It can be ran after
- exporting a bookmarks.html file from Chrome
- "clearning" html (I used https://html-cleaner.com/)'''

    args = get_args(
        description_str,
        {
            "flag": "html_file",
            "help": "chrome html file"
        },
        {
            "flag": "-o",
            "help": "full output file path and name"
        }
        )

    html_file = args.html_file
    output_location = args.o
    if not output_location:
        output_filename = 'chrome_output.html'
        config = get_json_config()
        outputlocation = os.path.join(config['directories']['bookmarksRootDir'], output_filename)

    write_mode = 'w'
    create_file(outputlocation, write_mode, html_file, get_replaced_line)

if __name__ == '__main__':
    main()