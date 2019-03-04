#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
from visit_and_tag_md_links import App

# this import only works if you're in this directory
sys.path.insert(0, '../utils')
import file_utils
from get_config import get_json_config


def debug(obj):
    '''{name: data}'''
    for name in obj.keys():
        print('{}: {}'.format(name, obj[name]))


def get_file_arr(file_path):
    with open(file_path) as f:
        return f.readlines()


def get_timestamp():
    import time
    time.sleep(.01)
    return str(int(time.time() * 1000))[4:]


def get_new_filepath(old_file):
    import os
    filename, file_extension = os.path.splitext(old_file)
    new_filename = filename + get_timestamp() + file_extension
    return new_filename


def write_sorted_file(new_filename, header_str, links_list):
    with open(new_filename, 'w') as new_file:
        new_file.write(header_str)
        for obj in links_list:
            new_file.write('\n\n' + obj['header'] + '\n')
            for line in obj['data']:
                new_file.write(line.strip() + '\n')
    print('Organized links:\n\t', new_filename)


def write_remaining(new_filename, remaining_list):
    with open(new_filename, 'w') as new_file:
        for line in remaining_list:
            new_file.write(line)
    print('Unorganized links:\n\t', new_filename)


def main():
    if len(sys.argv) < 2:
        sys.exit('error: Please enter a text/markdown filepath.')
    md_file = sys.argv[1]
    links = App(get_file_arr(md_file))
    links.block_encoder()
    headerList = links.get_sorted_headers(string=True)
    organizedLinks = links.organized_list
    newFileName = get_new_filepath(md_file)

    write_sorted_file(newFileName, headerList, organizedLinks)

    newFileName2 = get_new_filepath(md_file)
    remainingList = links.remaining_list
    write_remaining(newFileName2, remainingList)


if __name__ == '__main__':
    main()
