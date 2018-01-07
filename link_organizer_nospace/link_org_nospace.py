#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 7/25/17

@author: davecohen

Title: Markdown link organizer
    Given list of markdown links, each link is visited in your default browser,
    then you can "tag" the link in the terminal.
    output format from my markdown encoder
    see example below for the expected in format
    - no spaces between each link.
"""
# import itertools
# from pprint import pprint
import re
import webbrowser
import pyperclip


class App:

    # linkRegex = re.compile(r'(https?\:\/\/[^)]*)')
    linkRegex = re.compile(r'(\()(https?\:\/\/[^)]*)(\))')

    def __init__(self, in_list):
        self.in_list = in_list
        self.data_blocks = []
        self.header_list = []

    def block_encoder(self):
        '''Given bookmarks in markdown format (as list), a list of dicts with header and data is returned.
        '''
        # blocks = [list(g[1]) for g in itertools.groupby(todoArray, key= lambda x: x.strip() != '') if g[0]]

        for line in self.in_list:
            if len(line) <= 0:
                continue
            if line[0] == '*':
                self.visit_link(line)
                print(line)
                #add a custom header or hit enter to add a default zzzzz
                headerIn = self.header_input()
                if headerIn not in ['', 'quit']:
                    self.header_list.append(headerIn)
                    self.data_blocks.append({'header': headerIn, 'data': line})
                elif headerIn == '':
                    self.data_blocks.append({'header': 'zzzzz', 'data': line})
                elif headerIn.lower() == 'quit':
                    break
        # print() #debug
        #sort and overwrite dataBlocks...
        self.data_blocks = sorted(self.data_blocks, key=lambda k: k['header'].lower())
        # return dataBlocks
        # pprint(dataBlocks)

    def visit_link(self, str_url):
        # FYI - link regex - (https?\:\/\/[^)]*)
        # linkRegex = re.compile(r'(https?\:\/\/[^)]*)')
        link_mo = self.linkRegex.search(str_url)
        if link_mo:
            #open link if found
            webbrowser.open(link_mo.group(2))

    @staticmethod
    def header_input():
        print('Type in a header - optional. \'Quit\' to stop.')
        headerIn = input('> ').lower()
        return headerIn


    def print_sorted(self):
        #print sorted data
        for block in self.data_blocks:
            if block['header'] != 'zzzzz':
                print(block['header'])
            print(block['data'])
            # for line in block['data']:
            #     if line.strip()[0] not in ['#']:
            #         print(line)
            print()

    def return_sorted(self):
        #return sorted data for pyperclip
        sorted_r = []

        for block in self.data_blocks:
            if block['header'] != 'zzzzz':
                sorted_r.append(block['header'])
            sorted_r.append(block['data'])
            # for line in block['data']:
            #     if line.strip()[0] not in ['#']:
            #         print(line)
            sorted_r.append('')

        return '\n'.join(sorted_r)

def main():
    print('Copy your markdown links to clipboard, enter when done:')
    input('> ')
    todoTxt = pyperclip.paste()
    todoArray = todoTxt.split('\n')

    # encodedTodos = []
    # blocks = blockEncoder()
    links = App(todoArray)
    links.block_encoder()
    print('\n'*20, 'Finished!\n\n\n')
    headerList = ', '.join(links.header_list)
    allLinks = links.return_sorted()
    pyperclip.copy(headerList + '\n\n' + allLinks)
    print('Sorted links were copied to your clipboard.')

if __name__ == '__main__':
    main()