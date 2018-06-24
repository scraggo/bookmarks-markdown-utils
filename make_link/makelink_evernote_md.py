#pythontemplate
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on

@author: davecohen

Title: URL to Markdown URL List element
"""

#paste links here:
links = '''site title | site.com

[http://example.com](http://example.com) - site description here...
'''

# links = input('paste links here.')

linklist = links.split('\n')

newformat = []
for line in linklist:
    if line == '':
        continue
    if 'a' <= line[0].lower() <= 'z' or '0' <= line[0] <= '9':
        newformat.append('\n\n* {} - '.format(line))
    if line.startswith('['):
        newformat.append(line)
print(''.join(newformat))
