#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from onetab_to_markdown import App

# paste links here:
testlinks = '''
chrome-extension://klbibkeccnjlkjkiokjodocebajanakg/suspended.html#ttl=EbookFoundation%2Ffree-programming-books%3A%20Freely%20available%20programming%20books&uri=https://github.com/EbookFoundation/free-programming-books | EbookFoundation/free-programming-books: Freely available programming books
https://example1.com | site title1
https://example2.com | site title2
'''


def test_init():
    inst = App(testlinks)
    print(inst.in_list)


def test_re_search():
    inst = App(testlinks)
    for line in inst.in_list:
        print(inst.re_search(line))


def test_makelink():
    inst = App(testlinks)
    inst.make_link()
    print(inst.out_list)


def test_full():
    inst = App(testlinks)
    mdlinks = inst.return_links()
    print('\n'*20, 'Finished!\n\n\n')
    # input('Press Enter to copy sorted links to your clipboard.')
    print(mdlinks)


def run_tests():
    # print(testlinks)
    # test_init()
    # test_re_search()
    # test_makelink()
    test_full()


run_tests()
