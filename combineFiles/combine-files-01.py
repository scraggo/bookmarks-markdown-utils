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
outfilename = 'outfile.html'
filetype = '.html'

outfilepath = p.join(filepath, outfilename)
filenames = listdir(filepath)
# print(filenames)

# Combines files with specified filetype
with open(outfilepath, 'w') as outfile:
    for fname in filenames:
        if not fname.endswith(filetype): continue
        if fname == outfilename: continue
        fname = p.join(filepath, fname)
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
                
print('Success. see', outfilepath)