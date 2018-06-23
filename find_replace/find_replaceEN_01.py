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

<div><br/> with --- (or something)
<p> </p> (or whatever)
<div> and </div>
empty space
"""
import os, json

from replacer import replacer

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

print('Paste path to cleaned HTML (txt) file here:')
textfile = input('')

# don't need?
# textfile = textfile.split('\n')

config = None
with open("config.json", "r") as read_file:
    config = json.load(read_file)

outputlocation = os.path.join(config['outputDir'], '-pythonclean.html')
output = open(outputlocation, 'w')

with open(textfile) as f:
    for line in f:
        line = line.strip()
        line = get_replaced_line(line)
        output.write(line)

output.close()
print('Output to:', outputlocation)

# for line in textfile:
#     print(line)
#     print(replacer(line))
    

