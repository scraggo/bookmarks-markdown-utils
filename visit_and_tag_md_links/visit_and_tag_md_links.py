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

Needs work:
    Block encoder - split into two or more methods: 
        tag_links and block_encoder
    Private methods for the vars in __init__ (so I can sort and return them, keeping immutable)
"""
# import itertools
# from pprint import pprint
import re, webbrowser

class App:

    # linkRegex = re.compile(r'(https?\:\/\/[^)]*)')
    linkRegex = re.compile(r'(\()(https?\:\/\/[^)]*)(\))')

    def __init__(self, in_list):
        self.in_list = in_list
        self.data_blocks = []
        self.organized_list = []
        self.header_map = {}
        self.remaining_list = []
        self.DEFAULT_CHAR = '~~~NoTag~~~'

    def block_encoder(self):
        '''Given bookmarks in markdown format (as list), a list of dicts with header and data is returned.
        '''
        # blocks = [list(g[1]) for g in itertools.groupby(todoArray, key= lambda x: x.strip() != '') if g[0]]

        line_num_w_data = -1
        line_num = -1
        for line in self.in_list:
            line_num += 1
            line = line.strip()
            if len(line) <= 0:
                continue
            if line[0] == '*':
                line_num_w_data += 1
                self.visit_link(line)
                print(line)
                #add a custom header or hit enter to add DEFAULT
                headerIn = self.header_input()
                if headerIn.lower() == '.quit':
                    # append remaining lines to data blocks
                    # self.append_remaining_lines(line_num_w_data, line_num)
                    self.get_remaining_lines(line_num)
                    break
                elif headerIn == '':
                    self.update_header_and_data(self.header_map, self.DEFAULT_CHAR, self.data_blocks, line)
                else:
                    self.update_header_and_data(self.header_map, headerIn, self.data_blocks, line)

        self.organized_list = self.sort_data_list(self.data_blocks)

    @staticmethod
    def pprintObj(obj):
        import pprint
        pprint.pprint(obj)

    # def append_remaining_lines(self, line_num_w_data, line_num):
    #     emptyHeaderIdx = self.header_map.get(self.DEFAULT_CHAR, -1)
    #     if emptyHeaderIdx == -1:
    #         self.data_blocks.append({
    #             'header': self.DEFAULT_CHAR,
    #             'data': []
    #         })
    #         emptyHeaderIdx = len(self.data_blocks) - 1
    #         # print(emptyHeaderIdx, line_num_w_data)
    #         # print(self.in_list[line_num:line_num+3])
    #         # print(self.data_blocks[emptyHeaderIdx])
    #     self.data_blocks[emptyHeaderIdx]['data'] += self.in_list[line_num:]
    
    def get_remaining_lines(self, line_num):
      self.remaining_list = self.in_list[line_num:]

    @staticmethod
    def update_header_and_data(obj, header, dataList, data):
        if obj.get(header, False) is False:
            idx = len(dataList)#last available idx
            obj[header] = idx
            newObj = {
                'header': header,
                'data': [data]
            }
            dataList.append(newObj)
        else:
            idx = obj[header]
            dataList[idx]['data'].append(data)

    @staticmethod
    def sort_data_list(data_list):
        return sorted(data_list, key=lambda k: k['header'].lower())

    def visit_link(self, str_url):
        # FYI - link regex - (https?\:\/\/[^)]*)
        # linkRegex = re.compile(r'(https?\:\/\/[^)]*)')
        link_mo = self.linkRegex.search(str_url)
        if link_mo:
            #open link if found
            webbrowser.open(link_mo.group(2))

    @staticmethod
    def header_input():
        print('Type in a header - optional. \'.quit\' to stop.')
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

    def return_sorted(self, string = True):
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

        if string:
            return '\n'.join(sorted_r)
        else:
            return sorted_r

    def get_sorted_headers(self, string = True):
        # headerList = list(set(self.organized_list))
        headerList = sorted(self.header_map.keys())
        if string:
            return ', '.join(headerList)
        else:
            return headerList


