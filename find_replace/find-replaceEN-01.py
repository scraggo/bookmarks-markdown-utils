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
import os

def deleter(str):
    str = str\
    .replace('<div> </div>', '')\
    .replace('<p></p>', '')     \
    .replace('<div>', '')       \
    .replace('</div>', '')
    return str
    
def replacer(str):
    str = str                  \
    .replace('<a', '</p>\n<a')    \
    .replace('</a>', '</a>\n - ')  \
#     .replace('<dt>', '<li>')    \
#     .replace('</dt>', '</li>')
#     .replace('\n\n\n', '\n')
    return str

print('Paste path to cleaned HTML (txt) file here:')
textfile = input('')
# textfile = '/Users/davecohen/Dropbox/Notes/-BookmarkProject/BookmarkExports/bookmarks_4_26_17.html'

# don't need?
# textfile = textfile.split('\n')

outputlocation = os.path.join('/Users/davecohen/Dropbox/Notes/-BookmarkProject', '-pythonclean.html')
output = open(outputlocation, 'w')

with open(textfile) as f:
    for line in f:
        line = line.strip()
        line = line.replace('<div><br/>', '<p>')
        line = deleter(line)
        line = line.strip()
        if line != '':
#             print(replacer(line))
            output.write(replacer(line)+'\n')
output.close()
print('Output to:', outputlocation)

# for line in textfile:
#     print(line)
#     print(replacer(line))
    

