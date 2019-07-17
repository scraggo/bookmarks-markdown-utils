#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: davecohen
Title: Convert Firefox HTML exported bookmarks to Markdown Links
"""
import os
import html2text


def get_html_path():
    """For now..."""
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    html_path = os.path.join(desktop, 'bookmarks.html')
    return html_path


def get_html_converter():
    text_maker = html2text.HTML2Text()
    text_maker.ignore_tables = True
    text_maker.body_width = 0
    return text_maker


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
    with open(get_html_path(), encoding='utf-8') as html:
        # <file_blob>.read() => turn file into a string.
        html_string = html.read()
        raw_markdown = get_raw_markdown(html_string)
        formatted_markdown = get_formatted_markdown(raw_markdown)
        print(formatted_markdown)


if __name__ == '__main__':
    main()
