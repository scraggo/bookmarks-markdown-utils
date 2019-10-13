#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: davecohen
Title: Convert Firefox HTML exported bookmarks to Markdown Links
"""
import html2text
import sys
import os

# this import only works if you're in this directory
sys.path.insert(0, '../utils')
import date_append as DA
from get_config import get_config_path
from file_utils import FileUtils

fileutils = FileUtils()

html_path = get_config_path('directories', 'firefoxHTML')
md_path = get_config_path('directories', 'firefoxMD')
OUT_NAME = 'ff_backup.md'


def get_output_filename(infile, filename):
    ''' @returns {string} ex. _firefoxMD/ff_backup-191012.md '''
    new_dir_created = fileutils.make_dir_if_not_exists(md_path)
    output_filename = os.path.join(md_path, filename)
    output_filename = DA.date_append(output_filename)
    # print(output_filename)
    # a slight optimization. Don't check if file exists if dir didn't exist.
    if not new_dir_created:
        fileutils.fileExists(output_filename)  # raises error if exists
    return output_filename


def get_html_converter():
    converter = html2text.HTML2Text()
    converter.body_width = 0
    return converter


def get_raw_markdown(html):
    return get_html_converter().handle(html)


def format_raw_markdown_line(line):
    if line.startswith('['):
        return '* [' + line[1:].replace('[', '\n* [')
    return line


def get_formatted_markdown(raw_markdown):
    formatted_text = map(format_raw_markdown_line, raw_markdown.split('\n'))
    return '\n'.join(formatted_text)


def main():
    output_filename = get_output_filename(md_path, OUT_NAME)
    with open(html_path, encoding='utf-8') as html, open(output_filename, 'w') as output:
        # <file_blob>.read() => turn file into a string.
        html_string = html.read()
        raw_markdown = get_raw_markdown(html_string)
        formatted_markdown = get_formatted_markdown(raw_markdown)
        output.write(formatted_markdown)
        print('File written to', output_filename)


if __name__ == '__main__':
    main()
