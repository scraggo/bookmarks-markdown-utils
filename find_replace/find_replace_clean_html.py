#pythontemplate
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 4/26/17, 11:18 AM

@author: davecohen

usage:
'python find_replace_clean_html.py <html file> [-a APPEND]'

optional:
-a      APPEND to output instead of overwrite

Title: Find / Replace in HTML

Description:
This script finds and replaces or removes certain html tags.
It can be ran after
- exporting a bookmarks.html file from Chrome
- "clearning" html (I used https://html-cleaner.com/)
"""
import os, json, sys

from replacer import replacer

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

def create_file(outputlocation, write_mode, textfile, replace_func):
    output = open(outputlocation, write_mode)

    with open(textfile) as f:
        for line in f:
            line = line.strip()
            line = replace_func(line)
            output.write(line)
    output.close()
    print('Output to:', outputlocation)

def main():
    textfile = sys.argv[1]

    # add to main config.json
    config = None
    with open("config.json", "r") as read_file:
        config = json.load(read_file)

    outputlocation = os.path.join(config['outputDir'], 'outputfile.html')

    write_mode = 'w'
    if len(sys.argv) > 2:
        write_mode = 'a'

    create_file(outputlocation, write_mode, textfile, get_replaced_line)

if __name__ == '__main__':
    main()