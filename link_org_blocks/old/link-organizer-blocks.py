#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 7/25/17

@author: davecohen

Title: Markdown link organizer
    see example below for the expected in format
    - spaces between each link determine 'blocks'
    - non-special chars are headers.
"""
import itertools
from pprint import pprint
import pyperclip

todoTxt2 = '''
# MOBILE LINKS
## 2017 - May and June

Priority 1: search !!!
Chrome Extension
Lots of JavaScript in here. (?)
run the chrome-extension regex.

# 5/24/2017

Web Dev
* [Teach me English, I'll teach you web development](https://www.reddit.com/r/webdev/comments/6byrzp/teach_me_english_ill_teach_you_web_development/) | [https://www.reddit.com/r/webdev/comments/6byrzp/teach_me_english_ill_teach_you_web_development/](https://www.reddit.com/r/webdev/comments/6byrzp/teach_me_english_ill_teach_you_web_development/)


A cool looking app / similar to my idea
* [[macOS] Workspaces (beta) - an app that recreates working environment](https://www.reddit.com/r/webdev/comments/6ca3ts/macos_workspaces_beta_an_app_that_recreates/) | [https://www.reddit.com/r/webdev/comments/6ca3ts/macos_workspaces_beta_an_app_that_recreates/](https://www.reddit.com/r/webdev/comments/6ca3ts/macos_workspaces_beta_an_app_that_recreates/)


# 170531

Meetup!
* [Where Can I Find The Chicago Web Community?](https://www.reddit.com/r/webdev/comments/6drzro/where_can_i_find_the_chicago_web_community/) | [https://www.reddit.com/r/webdev/comments/6drzro/where_can_i_find_the_chicago_web_community/](https://www.reddit.com/r/webdev/comments/6drzro/where_can_i_find_the_chicago_web_community/)

Python / OOP
* [PyBites: Code Challenge 20 - Object Oriented Programming Fun - Review](http://pybit.es/codechallenge20_review.html) | [http://pybit.es/codechallenge20_review.html](http://pybit.es/codechallenge20_review.html)

JavaScript / FCC
* [If I finish all certificates on freeCodeCamp, how long will I have to wait to start working on a n… by Quincy Larson](https://www.quora.com/If-I-finish-all-certificates-on-freeCodeCamp-how-long-will-I-have-to-wait-to-start-working-on-a-nonprofit-project/answer/Quincy-Larson?share=8f15f623&srid=4tK5) | [https://www.quora.com/If-I-finish-all-certificates-on-freeCodeCamp-how-long-will-I-have-to-wait-to-start-working-on-a-nonprofit-project/answer/Quincy-Larson?share=8f15f623&srid=4tK5](https://www.quora.com/If-I-finish-all-certificates-on-freeCodeCamp-how-long-will-I-have-to-wait-to-start-working-on-a-nonprofit-project/answer/Quincy-Larson?share=8f15f623&srid=4tK5)

WebDev
* [“My path to web development”](https://www.reddit.com/r/learnprogramming/comments/6djovj/my_path_to_web_development/) | [https://www.reddit.com/r/learnprogramming/comments/6djovj/my_path_to_web_development/](https://www.reddit.com/r/learnprogramming/comments/6djovj/my_path_to_web_development/)


Music project / collaborate?
* [Random lyrics generator...](https://www.reddit.com/r/learnpython/comments/6dieqr/random_lyrics_generator/) | [https://www.reddit.com/r/learnpython/comments/6dieqr/random_lyrics_generator/](https://www.reddit.com/r/learnpython/comments/6dieqr/random_lyrics_generator/)

Python / code skeleton
* [Up for a little code review? Please criticize my first Git commit.](https://www.reddit.com/r/learnpython/comments/6dkjbb/up_for_a_little_code_review_please_criticize_my/) | [https://www.reddit.com/r/learnpython/comments/6dkjbb/up_for_a_little_code_review_please_criticize_my/](https://www.reddit.com/r/learnpython/comments/6dkjbb/up_for_a_little_code_review_please_criticize_my/)

Regex resources
* [If you struggle with REGULAR EXPRESSIONS, here is an awesome site that helps you understand them really quickly](https://www.reddit.com/r/learnprogramming/comments/6d93fs/if_you_struggle_with_regular_expressions_here_is/) | [https://www.reddit.com/r/learnprogramming/comments/6d93fs/if_you_struggle_with_regular_expressions_here_is/](https://www.reddit.com/r/learnprogramming/comments/6d93fs/if_you_struggle_with_regular_expressions_here_is/)

Interesting reading.
* [Looking for most enjoyed non-Python languages used by Python developers](https://www.reddit.com/r/Python/comments/6d5yn3/looking_for_most_enjoyed_nonpython_languages_used/) | [https://www.reddit.com/r/Python/comments/6d5yn3/looking_for_most_enjoyed_nonpython_languages_used/](https://www.reddit.com/r/Python/comments/6d5yn3/looking_for_most_enjoyed_nonpython_languages_used/)

some service
* [42 Exp - Find a team for your project idea](https://42exp.com/) | [https://42exp.com/](https://42exp.com/)
'''
print('Copy your notes to clipboard, enter when done:')
pause = input('> ')
todoTxt = pyperclip.paste()
todoArray = todoTxt.split('\n')

encodedTodos = []

def blockEncoder():
    '''Given bookmarks in markdown format (as list), a list of dicts with header and data is returned.
    '''
    blocks = [list(g[1]) for g in itertools.groupby(todoArray, key= lambda x: x.strip() != '') if g[0]]
    # pprint(blocks)

    dataBlocks = []
    for sublist in blocks:
        if sublist[0][0] not in ['#', '*']:
            dataBlocks.append({'header': sublist[0], 'data': sublist[1:]})
        else:
            #add a custom header or hit enter to add a default zzzzz
            for s in sublist:
                print(s)
            headerIn = headerInput()
            if headerIn != '':
                dataBlocks.append({'header': headerIn, 'data': sublist})
            else:
                dataBlocks.append({'header': 'zzzzz', 'data': sublist})
    # print() #debug
    #sort and overwrite dataBlocks...
    dataBlocks = sorted(dataBlocks, key=lambda k: k['header'].lower())
    return dataBlocks
    # pprint(dataBlocks)

def headerInput():
    print('Type in a header - optional.')
    headerIn = input('> ')
    return headerIn

#print sorted data
blocks = blockEncoder()
for block in blocks:
    if block['header'] != 'zzzzz':
        print(block['header'])
    for line in block['data']:
        if line.strip()[0] not in ['#']:
            print(line)
    print()