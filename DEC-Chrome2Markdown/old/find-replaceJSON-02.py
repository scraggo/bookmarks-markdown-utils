#pythontemplate
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 4/26/17, 11:18 AM

@author: davecohen

Title: Find / Replace in HTML

parsing:
delete: "type": "url",
replace: 

if line.startswith("name"):
    line.replace('"name": "', '* [')
    line.replace('",', ']')
if line.startswith("url"):
    line.replace('"url": "', '(')
    line.replace('",', ')')

"name": with [ ]
"url": with ( )

example:
"name": "UPS: Register",
"url": "chrome-extension://klbibkeccnjlkjkiokjodocebajanakg/suspended.html#uri=https://www.ups.com/one-to-one/login"

want: 
* [UPS: Register](chrome-extension://klbibkeccnjlkjkiokjodocebajanakg/suspended.html#uri=https://www.ups.com/one-to-one/login)

"""
import os, sys, re

def deleter(str):
    str = str\
    .replace('"type": "url",', '')
    return str
    
def replacer(str):
    str = str                  \
    .replace('<a', '</p>\n<a')    \
    .replace('</a>', '</a>\n - ')  \
#     .replace('<dt>', '<li>')    \
#     .replace('</dt>', '</li>')
#     .replace('\n\n\n', '\n')
    return str


# textfile = input('')
textfile = '/Users/davecohen/Library/Application Support/Google/Chrome/Default/Bookmarks'
print('Copying: ' + textfile)

# don't need?
# textfile = textfile.split('\n')

outputlocation = os.path.join('/Users/davecohen/Dropbox/Notes/-BookmarkProject', '--chrome-date.md')
print('Save to ' + outputlocation + '?')
quit = input('Press y if ok. If not ok, press enter. ')
if quit != 'y':
    sys.exit('Quitting.')

output = open(outputlocation, 'w')

with open(textfile) as f:
    for line in f:
        line = line.strip()
        line = deleter(line)
        if line.startswith('"name"'):
            line = line.replace('"name": "', '* [')
            line = line.replace('",', ']')
            output.write(line)
        elif line.startswith('"url"'):
            if 'chrome-extension://' in line:
                line = re.sub(r"chrome-extension://([a-z])+/suspended.html#uri=", "", line)
            line = line.replace('"url": "', '(')
            line_paren = line.replace('"', ')')
            line = line_paren + ' | ' + line_paren.replace('(', '[').replace(')', ']') + line_paren
#             print(replacer(line))
            output.write(line + '\n')
output.close()
print('Output to:', outputlocation)

# for line in textfile:
#     print(line)
#     print(replacer(line))
    

'''
line = re.sub(r"chrome-extension://([a-z])+/suspended.html#uri=", "", line)
chrome-extension://([a-z])+/suspended.html#uri=
suspRegex = re.compile(r'chrome-extension://([a-z])+/suspended.html#uri=')
suspRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')

'''