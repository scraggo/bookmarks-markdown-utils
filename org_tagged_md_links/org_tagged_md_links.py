#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 7/25/17

@author: davecohen

Title: Markdown link organizer
    see example in test.py for the expected in format
    - spaces between each link determine 'blocks'
    - non-special chars are headers.
"""
import itertools
from pprint import pprint
import pyperclip

class App:

    LOWEST_CHAR = '~' * 10

    def __init__(self, input_text):
        self.input_list = input_text.split('\n')
        # self.block_list = self.make_blocks(self.input_list)
        self.encoded_list = []
        self.block_encoder()

    def block_encoder(self):
        '''Given bookmarks in markdown format (as list), a list of dicts with header and data is returned.
        '''
        # Make blocks
        blocks = [list(g[1]) for g in itertools.groupby(self.input_list, key= lambda x: x.strip() != '') if g[0]]
        # pprint(blocks)

        for sublist in blocks:
            if sublist[0][0] == '#':
                continue
            elif sublist[0][0] != '*':
                self.encoded_list.append({'header': sublist[0], 'data': sublist[1:]})
            else:
                print()
                #add a custom header or hit enter to add a default LOWEST_CHAR
                for s in sublist:
                    t = s.split('](')
                    if t[1]:
                        print('{}\n    {}'.format(t[0][3:], t[1][:-1]))
                headerIn = self.headerInput()
                if headerIn != '':
                    self.encoded_list.append({'header': headerIn, 'data': sublist})
                else:
                    self.encoded_list.append({'header': self.LOWEST_CHAR, 'data': sublist})
        print()
        # print() #debug
        #sort and overwrite self.encoded_list...
        self.encoded_list = sorted(self.encoded_list, key=lambda k: k['header'].lower())
        # pprint(self.encoded_list)

    @staticmethod
    def headerInput():
        print('Type in a header - optional.')
        headerIn = input('> ')
        return headerIn

    def returnTags(self):
        headers = map(lambda item: item['header'], self.encoded_list)
        return ', '.join(sorted(list(set(headers))))

    def return_sorted(self):
        #returns a string sorted data. make sure to run block_encoder first.
        sortedBlocks = []
        for block in self.encoded_list:
            if block['header'] != self.LOWEST_CHAR:
                sortedBlocks.append(block['header'])
            for line in block['data']:
                if line.strip()[0] not in ['#']:
                    sortedBlocks.append(line)
            sortedBlocks.append('')

        return '\n'.join(sortedBlocks)

def main():
    print('Copy your titled links to clipboard, enter when done:')
    pause = input('> ')
    orgLinks = pyperclip.paste()
    o = App(orgLinks)
    fullText = o.returnTags() + '\n\n' + o.return_sorted()
    # pyperclip.copy(o.return_sorted())
    pyperclip.copy(fullText)
    print('Your links were organized and copied to clipboard.')

if __name__ == '__main__':
    main()
