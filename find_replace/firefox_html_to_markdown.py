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
from get_config import get_json_config
from file_utils import FileUtils

fileutils = FileUtils()


def get_html_path():
    # get firefox html file
    return get_json_config()['directories']['firefoxHTML']


def get_output_filename(infile, filename):
    dir = os.path.dirname(infile)
    output_dir = os.path.join(dir, '_firefoxMD')
    new_dir_created = fileutils.make_dir_if_not_exists(output_dir)
    output_filename = os.path.join(output_dir, filename)
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
    html_path = get_html_path()
    output_filename = get_output_filename(html_path, 'ff_backup.md')
    with open(html_path, encoding='utf-8') as html, open(output_filename, 'w') as output:
        # <file_blob>.read() => turn file into a string.
        html_string = html.read()
        raw_markdown = get_raw_markdown(html_string)
        formatted_markdown = get_formatted_markdown(raw_markdown)
        output.write(formatted_markdown)
        print('File written to', output_filename)


if __name__ == '__main__':
    main()
