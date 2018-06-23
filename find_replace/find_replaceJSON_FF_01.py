#pythontemplate
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 4/26/17, 11:18 AM

@author: davecohen

Title: Convert Firefox Backup (JSON) to Markdown Links

"""
import os, sys, re, json

from replacer import replacer
from create_file import create_file

# this import only works if you're in this directory
sys.path.insert(0, '../utils')
from get_config import get_json_config

def get_replaced_line(line):
    '''This function is file-specific
    '''
    to_delete = [
        ['"type": "url",', '']
    ]

    to_replace_name = [
        ['"name": "', '* ['],
        ['",', ']']
    ]

    to_replace_paren = [
        ['(', '['],
        [')', ']']
    ]

    line = replacer(to_delete, line)
    if line.startswith('"name"'):
        return replacer(to_replace_name, line)
    elif line.startswith('"url"'):
        if 'chrome-extension://' in line:
            line = re.sub(r"chrome-extension://([a-z])+/suspended.html#uri=", "", line)
        line = line.replace('"url": "', '(')
        line_paren = line.replace('"', ')')
        line = line_paren + ' | ' + replacer(to_replace_paren, line_paren) + line_paren
        return line + '\n'
    return ''

def main():
    # get paths
    config = get_json_config()
    # load firefox json file
    with open(config['directories']['firefoxJson'], encoding='utf-8') as data_file:    
        data = json.loads(data_file.read())

    ff_json_list = str(data).split(', ')

    output_filename = 'firefox_output.html'
    outputlocation = os.path.join(config['directories']['bookmarksRootDir'], output_filename)


    if os.path.exists(outputlocation):
            print('Save over ' + outputlocation + '?')
            quit = input('Press y if ok. If not ok, press enter. ')
            if quit.lower() != 'y':
                sys.exit('Quitting.')

    create_file(outputlocation, 'w', ff_json_list, get_replaced_line)

if __name__ == '__main__':
    main()    
