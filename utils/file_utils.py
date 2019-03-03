#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import sys
# from chr_config import directories

# this import only works if you're in this directory
from get_config import get_json_config

directories = get_json_config()['directories']

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

    def join_path(self, top_dir, root_dir=None):
        if not root_dir:
            root_dir = directories['bookmarksRootDir']
        return os.path.join(root_dir, top_dir)

    def copy_file(self, file_path, new_dir):
        fileName = os.path.split(file_path)[1]
        self.fileExists(os.path.join(new_dir, fileName))
        return shutil.copy(file_path, new_dir)

    # def rename_file(self, input_file_path, new_file_name):
    #   output = self.join_path(directories[top_dir])
    #   self.fileExists(output)
    #   # print(input_file_path, output)
    #   shutil.copy(input_file_path, output)
    #   if new_file_name:
    #     new_output = os.path.join(output, new_file_name)
    #   self.fileExists(new_output)
    #   return os.rename(output, new_output)

    def move_to_mobileLinksDir(self, input_file_path):
        output = self.join_path(directories['mobileLinksDir'])
        return shutil.move(input_file_path, output)

    def copy_to_markdownBackupsDir(self, input_file_path):
        output = self.join_path(directories['markdownBackupsDir'])
        return shutil.copy(input_file_path, output)

    def copy_to_chrJsonBackupsDir(self, input_file_path, new_file_name):
        newDest = self.join_path(directories['chrJsonBackupsDir'])
        # oldFileName = os.path.split(input_file_path)[1]
        # self.copy_file(input_file_path, newDest)
        oldNameNewDest = self.copy_file(input_file_path, newDest)
        newFilePath = os.path.join(newDest, new_file_name)
        os.rename(oldNameNewDest, newFilePath)
        return newFilePath
