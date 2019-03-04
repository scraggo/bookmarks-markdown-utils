# pythontemplate
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

help = """
Title: Onetab export to Markdown URL List element

Description: Copy links to clipboard in the input format. They'll be sent to your clipboard in the output format.

Example input:
https://example1.com | site title1
https://example2.com | site title2

Example output:
* [https://example1.com](https://example1.com)
* [https://example2.com](https://example2.com)
"""

import re
import string
import sys
import pyperclip
sys.path.insert(0, '../utils')
import arg_utils


class App:

    linkRegex = re.compile(r'(https?\S*)( \| )(.*)')
    suspRegex = r"(chrome-extension://)(.+)(uri=)"
    # printable = set(string.printable)

    def __init__(self, in_text):
        # remove non-ascii - not working
        # self.in_text = ''.join(filter(lambda x: ord(x) <= 126, in_text))
        self.in_text = re.sub(self.suspRegex, '', in_text)
        self.in_list = in_text.split('\n')
        self.out_list = []
        self.make_link()

    def make_link(self):
        for line in self.in_list:
            found_links = self.re_search(line)
            if found_links:
                md_link = '* [{}]({})'.format(found_links[1], found_links[0])
                self.out_list.append(md_link)
            else:
                self.out_list.append(line.replace('http://', '## '))

    def return_links(self):
        return '\n'.join(self.out_list)

    def re_search(self, f_line):
        link_mo = self.linkRegex.search(f_line)
        if link_mo:
            # open link if found
            return link_mo.group(1), link_mo.group(3)
        return None


def main():
    arg_utils.show_help_if_arg(sys.argv, help)
    print('Copy your markdown links to clipboard, enter when done:')
    input('> ')
    linkTxt = pyperclip.paste()

    links = App(linkTxt)
    links.make_link()
    print('\n'*20, 'Finished!\n\n\n')
    input('Press Enter to copy sorted links to your clipboard.')
    pyperclip.copy(links.return_links())


if __name__ == '__main__':
    main()
