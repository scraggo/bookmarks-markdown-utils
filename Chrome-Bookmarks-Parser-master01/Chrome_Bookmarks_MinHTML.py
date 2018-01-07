#!/usr/bin/env python

""" A script that parses the Bookmarks.bak json and outputs it
as a compatible .html file that Chrome can import again.

Credits to Matt Jones (mattCreative)'s PHP script which served 
as the framework for this one.
https://github.com/mattCreative/chrome-bookmarks-converter
"""
import json

__author__ = "David Metcalfe"
__copyright__ = "Copyright 2017"
__credits__ = ["David Metcalfe", "Matt Jones"]

__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "David Metcalfe"
__status__ = "Production"

def main():

    header = '''<!DOCTYPE NETSCAPE-Bookmark-file-1>
    <!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
    <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
    <TITLE>Bookmarks</TITLE>
    <H1>Bookmarks</H1>
    <DL><p>\n'''

    def deeper(array, depth = 0, max_depth = False):
        if max_depth and depth == max_depth:
            return

        for node in array:
            if 'children' in node:
                writeIt('<h3>' + node['name'] + '</h3>', depth)
#                 writeIt('<DL><p>', depth)
#                 writeIt('<ul>', depth)
                deeper(node['children'], depth + 1, max_depth)
#                 writeIt('</DL><p>', depth)
#                 writeIt('</ul>', depth)
            elif 'url' in node:
                writeIt('<a href="' + node['url'] + '">' + node['name'] + '</a><br>', depth)


    def writeIt(line, depth = 0):
        tab = "    "
        for i in range(depth):
            line = tab + line

        outf.write(line + "\n")

    with open('Bookmarks.bak', 'r', encoding='utf8') as inf:
        with open('Bookmark_backup.html', 'w', encoding='utf8') as outf:
            workingData = json.load(inf)
            writeIt(header)

            if workingData['roots']['bookmark_bar']:
                writeIt('<h3>Bookmarks bar</h3>')
#                 writeIt('<DL><p>')
                deeper(workingData['roots']['bookmark_bar']['children'], 1, 10)
#                 writeIt('</DL><p>')

            if workingData['roots']['other']:
                writeIt('<h3>Other bookmarks</h3>')
#                 writeIt('<DL><p>')
                deeper(workingData['roots']['other']['children'], 1, 10)
#                 writeIt('</DL><p>')

if __name__ == "__main__":
    main()