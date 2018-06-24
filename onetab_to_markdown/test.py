#pythontemplate
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from onetab_to_markdown import App

#paste links here:
testlinks = '''
http://---MIDI
https://mail.google.com/mail/u/0/?tab=wm#inbox | Inbox (1,433) - dcohen18@gmail.com - Gmail
chrome-extension://klbibkeccnjlkjkiokjodocebajanakg/suspended.html#ttl=EbookFoundation%2Ffree-programming-books%3A%20Freely%20available%20programming%20books&uri=https://github.com/EbookFoundation/free-programming-books | EbookFoundation/free-programming-books: Freely available programming books
chrome-extension://klbibkeccnjlkjkiokjodocebajanakg/suspended.html#ttl=Added%20reference%20to%20issue%20%232353%20in%20CONTRIBUTING%20by%20scraggo%20%C2%B7%20Pull%20Request%20%232521%20%C2%B7%20EbookFoundation%2Ffree-programming-books&uri=https://github.com/EbookFoundation/free-programming-books/pull/2521 | Added reference to issue #2353 in CONTRIBUTING by scraggo _ Pull Request #2521 _ EbookFoundation/free-programming-books
chrome-extension://klbibkeccnjlkjkiokjodocebajanakg/suspended.html#ttl=scraggo%2Ffree-programming-books%20at%20issue-2353&uri=https://github.com/scraggo/free-programming-books/tree/issue-2353 | scraggo/free-programming-books at issue-2353
chrome-extension://klbibkeccnjlkjkiokjodocebajanakg/suspended.html#ttl=CodePen%20Chicago%3A%20August%2028th%202017%20by%20Brian%20Montana%20on%20CodePen&uri=https://codepen.io/brianmontanaweb/post/codepen-chicago-august-28th-2017 | CodePen Chicago: August 28th 2017 by Brian Montana on CodePen
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