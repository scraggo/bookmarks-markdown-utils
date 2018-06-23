#pythontemplate
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 4/26/17, 11:18 AM

@author: davecohen

Title: Convert Firefox Backup (JSON) to Dave's Custom Markdown

"""
import os, sys, re, json

from replacer import replacer

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
    textfile = input('Path to Firefox backup JSON file:')

    print('Copying: ' + textfile)

    config = None
    with open("config.json", "r") as read_file:
        config = json.load(read_file)

    outputlocation = os.path.join(config['outputDir'], '--firefox-date.md')

    print('Save to ' + outputlocation + '?')
    quit = input('Press y if ok. If not ok, press enter. ')
    if quit != 'y':
        sys.exit('Quitting.')

    output = open(outputlocation, 'w')

    with open(textfile) as f:
        for line in f:
            line = line.strip()
            line = get_replaced_line(line)
            output.write(line)

    output.close()
    print('Output to:', outputlocation)

if __name__ == '__main__':
    main()    

'''
line = re.sub(r"chrome-extension://([a-z])+/suspended.html#uri=", "", line)
chrome-extension://([a-z])+/suspended.html#uri=
suspRegex = re.compile(r'chrome-extension://([a-z])+/suspended.html#uri=')
suspRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')

'''