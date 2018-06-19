#chr2mkdown.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Jun 16 2018

@author: davecohen

Title: Convert Chrome Bookmarks JSON file to Markdown
    and backup Chrome Bookmarks

Dependencies:
    chr_backup.py
    chr_config.py
    chr_path.py
    date_append.py

Output Format:
* [UPS: Register](https://www.ups.com/one-to-one/login) | [https://www.ups.com/one-to-one/login](https://www.ups.com/one-to-one/login)

Input Example:
"name": "UPS: Register",
"url": "chrome-extension://klbibkeccnjlkjkiokjodocebajanakg/suspended.html#uri=https://www.ups.com/one-to-one/login"

parsing:
delete: "type": "url",
replace: 
"name": with [ ]
"url": with ( )

"""

#Standard library:
import os
import subprocess

from chr_backup import chrBackup
from chr2mkdown import MarkdownCreator
from move_files import move_files
import chr_config

def test_things():
  md_creator = MarkdownCreator()
  # md_creator.run_script()
  md_creator.create_output_path()
  new_file_path = md_creator.md_output
  path, file_name = os.path.split(new_file_path)
  print(path, file_name)

def main():

  chrBackup()  #Backup bookmarks

  md_creator = MarkdownCreator()
  md_creator.run_script()
  new_file_path = md_creator.md_output
  # path, file_name = os.path.split(new_file_path)
  # print('Split up the path and file name:\n', path, file_name)
  # move_files(new_file_path)
  subprocess.run(['node', chr_config.node_scripts['deleteLeadingText'], new_file_path])


if __name__ == '__main__':
  # test_things()
  main()



