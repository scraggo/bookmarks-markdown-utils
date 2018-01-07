#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 7/25/17

@author: davecohen

Title: Markdown link organizer
    output format from my markdown encoder
    see example below for the expected in format
    - no spaces between each link.
"""
# import itertools
# from pprint import pprint
import pyperclip
import webbrowser
import re

# todoTxt = \
'''
* [Mobile-Keep]* [Other Bookmarks]* [---MOBILE-BOOKMARKS](about:blank) | [about:blank](about:blank)
* [When am I experienced enough to apply for internships?](https://www.reddit.com/r/cscareerquestions/comments/6o3he4/when_am_i_experienced_enough_to_apply_for/) | [https://www.reddit.com/r/cscareerquestions/comments/6o3he4/when_am_i_experienced_enough_to_apply_for/](https://www.reddit.com/r/cscareerquestions/comments/6o3he4/when_am_i_experienced_enough_to_apply_for/)
* [What are you guys using for styling form controls nowadays?](https://www.reddit.com/r/web_design/comments/6pphww/what_are_you_guys_using_for_styling_form_controls/) | [https://www.reddit.com/r/web_design/comments/6pphww/what_are_you_guys_using_for_styling_form_controls/](https://www.reddit.com/r/web_design/comments/6pphww/what_are_you_guys_using_for_styling_form_controls/)
* [O'Reilly is offering ebooks about UX, Data, IoT...](https://www.reddit.com/r/webdev/comments/6pgjg4/oreilly_is_offering_ebooks_about_ux_data_iot/) | [https://www.reddit.com/r/webdev/comments/6pgjg4/oreilly_is_offering_ebooks_about_ux_data_iot/](https://www.reddit.com/r/webdev/comments/6pgjg4/oreilly_is_offering_ebooks_about_ux_data_iot/)
* [SPAs vs MPAs/MVC - Are Single Page Apps always better?](https://www.reddit.com/r/webdev/comments/6phqhe/spas_vs_mpasmvc_are_single_page_apps_always_better/) | [https://www.reddit.com/r/webdev/comments/6phqhe/spas_vs_mpasmvc_are_single_page_apps_always_better/](https://www.reddit.com/r/webdev/comments/6phqhe/spas_vs_mpasmvc_are_single_page_apps_always_better/)
'''

class App:
    def __init__(self, in_list):
        self.in_list = in_list
        self.data_blocks = []

    def block_encoder(self):
        '''Given bookmarks in markdown format (as list), a list of dicts with header and data is returned.
        '''
        # blocks = [list(g[1]) for g in itertools.groupby(todoArray, key= lambda x: x.strip() != '') if g[0]]


        for line in self.in_list:
            if len(line) <= 0:
                continue
            if line[0] == '*':
                #link regex - (https?\:\/\/[^)]*)
                linkRegex = re.compile(r'(https?\:\/\/[^)]*)')
                link_mo = linkRegex.search(line)
                if link_mo:
                    #open link if found
                    webbrowser.open(link_mo.group(1))

                #add a custom header or hit enter to add a default zzzzz
                print(line)
                headerIn = self.header_input()
                if headerIn not in ['', 'quit']:
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
    input('Press Enter to copy sorted links to your clipboard.')
    pyperclip.copy(links.return_sorted())


if __name__ == '__main__':
    main()