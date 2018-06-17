#pythontemplate
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 4/26/17, 11:18 AM

@author: davecohen

Title: Find / Replace in HTML

Python or
https://html-cleaner.com/
set to remove empty tags
replace <p> </p>
    with nothing.
replace <dd> with nothing.
replace </dd> with nothing.

SAVE OUTPUT TO HTML FILE

Python or TEXTWRANGLER:
replace <dl> with <ul>
replace </dl> with </ul>
replace <dt> with <li>
replace </dt> with </li>
replace empty tags
"""
import os
import json

def deleter(str):
    str = str                   \
    .replace('<p></p>', '')     \
    .replace('<p> </p>', '')    \
    .replace('<dd>', '')        \
    .replace('</dd>', '')
    return str
    
def replacer(str):
    str = str                  \
    .replace('<dl>', '<ul>')    \
    .replace('</dl>', '</ul>')  \
    .replace('<dt>', '<li>')    \
    .replace('</dt>', '</li>')
#     .replace('\n\n\n', '\n')
    return str

print('Paste path to cleaned HTML (txt) file here:')
textfile = input('')

# don't need?
# textfile = textfile.split('\n')

config = None
with open("config.json", "r") as read_file:
    config = json.load(read_file)

outputlocation = os.path.join(config['outputDir'], 'outputfile.html')
output = open(outputlocation, 'a')

with open(textfile) as f:
    for line in f:
        line = line.strip()
        line = deleter(line)
        if line != '':
#             print(replacer(line))
            output.write(replacer(line)+'\n')
output.close()
print('Output to:', outputlocation)

# for line in textfile:
#     print(line)
#     print(replacer(line))
    

