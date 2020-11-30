# pythontemplate
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 4/26/17, 11:18 AM

@author: davecohen

Title: Convert Firefox Backup (JSON) to Markdown Links
"""
import os
import sys
import re
import json
from pprint import pprint

# this import only works if you're in this directory
sys.path.insert(0, '../utils')
from get_config import get_json_config


def deleter(str):
    if str.endswith("'") or\
            str.endswith("]") or\
            str.endswith("}"):
        return(deleter(str[:-1]))  # Note: this is recursive
    else:
        return str


def replacer(str):
    str = str                  \
        .replace('<a', '</p>\n<a')    \
        .replace('</a>', '</a>\n - ')
    return str


def main():
    # get paths
    config = get_json_config()

    # load firefox json file
    with open(config['directories']['firefoxJson'], encoding='utf-8') as data_file:
        data = json.loads(data_file.read())

    ff_json_list = str(data).split(', ')

    output_filename = 'firefox_output.html'
    outputlocation = os.path.join(
        config['directories']['bookmarksRootDir'], output_filename)

    if os.path.exists(outputlocation):
        print('Save over ' + outputlocation + '?')
        quit = input('Press y if ok. If not ok, press enter. ')
        if quit.lower() != 'y':
            sys.exit('Quitting.')

    with open(outputlocation, 'w') as output:
        for line in ff_json_list:
            line = line.strip()
            line = deleter(line)
            if line[1:6] == 'title' and len(line) > 11:
                line = '* [' + line[10:] + ']'  # was 10:-1
                output.write(line)
            elif line[1:4] == 'uri':
                line = '(' + line[8:] + ')'  # was 8:-2
                output.write(line + '\n')

    print('Output to:', outputlocation)


if __name__ == '__main__':
    main()
