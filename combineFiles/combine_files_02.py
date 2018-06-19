#pythontemplate
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 4/26/17, 11:18 AM

@author: davecohen

Title: Combine files

"""
import os
from os import listdir
from os import path as p

# Get file path
print('Paste path of files: ')
filepath = input('')

# These can be changed
outfilename = '--combined.html'
filetype = '.html'

outfilepath = p.join(filepath, outfilename)
filenames = listdir(filepath)
# print(filenames)

#generator - will this work in my program?
filegen = (x for x in filenames if x.endswith(filetype))
# print(filegen)
# for file in filegen:
#     print(file)

# Combines files with specified filetype
with open(outfilepath, 'w') as outfile:
    for fname in filegen:
#         if not fname.endswith(filetype): continue
        if fname == outfilename: continue
        fname = p.join(filepath, fname)
        with open(fname) as infile:
            for line in infile:
#                 pass
                outfile.write(line)
                
print('Success. see', outfilepath)