#!/usr/bin/env python3
# -*- coding: utf-8 -*-
help = """
Title: URL to Markdown URL List element

Description: Copy links to clipboard in the input format. They'll be sent to your clipboard in the output format.

Example input:
https://example1.com
https://example2.com

Example output:
* [https://example1.com](https://example1.com)
* [https://example2.com](https://example2.com)
"""

import re
import sys
# this import only works if you're in this directory
sys.path.insert(0, '../utils')
from pyperclip_interface import PyperInterface
import arg_utils


def reformat_links(linklist):
    newformat = []
    for line in linklist:
        line = line.strip()
        if line == '':
            continue
        else:
            newformat.append('* [{}]({})'.format(line, line))
    return newformat


def main():
    arg_utils.show_help_if_arg(sys.argv, help)
    in_message = 'Copy your URL links to clipboard, press ENTER when done:'
    out_message = 'Finished!\nMarkdown links were copied to your clipboard.'
    pyper = PyperInterface(in_message, out_message)

    links = pyper.get_clipboard()
    linklist = links.split('\n')

    reformatted = reformat_links(linklist)
    pyper.send_to_clipboard('\n'.join(reformatted))


if __name__ == '__main__':
    main()
