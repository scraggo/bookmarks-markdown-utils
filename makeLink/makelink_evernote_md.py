#pythontemplate
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on

@author: davecohen

Title: URL to Markdown URL List element
"""

#paste links here:
links = '''5 reasons NOT to use Twitter Bootstrap | Zing Design

[http://www.zingdesign.com/5-reasons-not-to-use-twitter-bootstrap/](http://www.zingdesign.com/5-reasons-not-to-use-twitter-bootstrap/) - Twitter Bootstrap is all the rage at the moment, but let's stop for a moment and have a look at the ways in which Twitter Bootstrap can fail

[X-POST from /r/learnjavascript] CSS Reference - A free visual guide to the most popular CSS properties • r/learnprogramming
'''

# links = input('paste links here.') #no idea why it doesn't work...

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

