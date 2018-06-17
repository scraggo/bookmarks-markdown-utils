#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shutil
from chr_config import directories
import os

'''
Calling shutil.move(source, destination) will move the file or folder at the path source to the path destination and will return a string of the absolute path of the new location.

If destination points to a folder, the source file gets moved into destination and keeps its current filename. For example, enter the following into the interactive shell:
'''

class FileUtils:
  # def __init__(self, input_file_path):
  #   self.input_file_path = input_file_path

  def fileExists(self, filePath):
    if os.path.exists(filePath):
      raise OSError(filePath + ' file exists.')

  def join_path(self, top_dir):
    return os.path.join(directories['bookmarksRootDir'], top_dir)

  def copy_rename_file(self, top_dir, input_file_path, new_file_name):
    output = self.join_path(directories[top_dir])
    if new_file_name:
      output = os.path.join(output, new_file_name)
    self.fileExists(output)
    return shutil.copy(input_file_path, output)

  def move_to_mobileLinksDir(self, input_file_path):
    output = self.join_path(directories['mobileLinksDir'])
    return shutil.move(input_file_path, output)  

  def copy_to_markdownBackupsDir(self, input_file_path):
    output = self.join_path(directories['markdownBackupsDir'])
    return shutil.copy(input_file_path, output)

  def copy_to_chrJsonBackupsDir(self, input_file_path, new_file_name = False):
    return self.copy_rename_file('chrJsonBackupsDir', input_file_path, new_file_name)
