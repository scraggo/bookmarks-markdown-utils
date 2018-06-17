#pythontemplate
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 

@author: davecohen

Title: URL to Markdown URL List element
"""

#paste links here:
links = '''https://dash.generalassemb.ly/
http://www.techaltair.com/free-online-courses-to-grow-your-tech-skills/
http://www.e-booksdirectory.com/programming.php
http://www.freeprogrammingresources.com/
http://www.oreilly.com/programming/free/
http://freevideolectures.com/blog/2010/07/20-cs-programming-online-courses-with-video-lectures/
http://www.onlinecollegecourses.com/2012/08/06/50-places-you-can-learn-to-code-for-free-online/
https://github.com/vhf/free-programming-books/blob/master/free-programming-books.md
'''

linklist = links.split('\n')

for line in linklist:
    print('* [{}]({})'.format(line, line))
    
#add pyperclip? doesn't run from textwrangler

'''
for line in linklist:
    if line.startswith('#'):
        print(line)
    else:
        print('* <{}> - '.format(line))

'''