#pythontemplate
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 4/26/17, 11:18 AM

@author: davecohen

Title: Convert Firefox Backup (JSON) to Dave's Custom Markdown

"""
import os, sys, re
import json
from pprint import pprint

def deleter(str):
    if str.endswith("'") or\
    str.endswith("]") or\
    str.endswith("}"):
        return(deleter(str[:-1])) #I used recursion!
    else:
        return str        

#     str = str\
#     .replace('"type": "url",', '')
#     return str
    
def replacer(str):
    str = str                  \
    .replace('<a', '</p>\n<a')    \
    .replace('</a>', '</a>\n - ')  \
#     .replace('<dt>', '<li>')    \
#     .replace('</dt>', '</li>')
#     .replace('\n\n\n', '\n')
    return str


JSONfile = input('Path to Firefox backup JSON file:')
# /Users/davecohen/Dropbox/Notes/-BookmarkProject/BookmarkExports/-firefox-json/bookmarks-2017-06-04.json

with open(JSONfile, encoding='utf-8') as data_file:    
    data = json.loads(data_file.read())

# pprint(data)
# print("LINE")
dataList = str(data).split(', ')
# print(dataList)
# sys.exit()

# don't need?
# textfile = textfile.split('\n')

outputlocation = os.path.join('/Users/davecohen/Dropbox/Notes/-BookmarkProject', '--firefox-date.md')
print('Save to ' + outputlocation + '?')
quit = input('Press y if ok. If not ok, press enter. ')
if quit != 'y':
    sys.exit('Quitting.')

output = open(outputlocation, 'w')

for line in dataList:
    line = line.strip()
#     print(line) #debug
    line = deleter(line)
    if line[1:6] == 'title' and len(line) > 11:
        line = '* [' + line[10:] + ']'      #was 10:-1
#         line = line.replace('"name": "', '* [')
#         line = line.replace('",', ']')
        output.write(line)
    elif line[1:4] == 'uri':
        line = '(' + line[8:] + ')'         #was 8:-2
#         line = line.replace('"url": "', '(')
#         line_paren = line.replace('"', ')')
#         line = line_paren + ' | ' + line_paren.replace('(', '[').replace(')', ']') + line_paren
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