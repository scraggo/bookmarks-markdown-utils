#pythontemplate
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 

@author: davecohen

Title: URL to Markdown URL List element
"""

#paste links here:
links = '''https://example1.com
https://example2.com
https://example3.com
'''

linklist = links.split('\n')

for line in linklist:
    print('* [{}]({})'.format(line, line))
