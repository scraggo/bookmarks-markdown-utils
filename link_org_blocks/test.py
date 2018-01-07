#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from link_org_blocks import *

ORG_LINKS = '''
# MOBILE LINKS
## 2017 - May and June

Priority 1: search !!!
Chrome Extension
Lots of JavaScript in here. (?)
run the chrome-extension regex.

# 5/24/2017

Web Dev
* [Teach me English, I'll teach you web development](https://www.reddit.com/r/webdev/comments/6byrzp/teach_me_english_ill_teach_you_web_development/) | [https://www.reddit.com/r/webdev/comments/6byrzp/teach_me_english_ill_teach_you_web_development/](https://www.reddit.com/r/webdev/comments/6byrzp/teach_me_english_ill_teach_you_web_development/)

* [subnotes-python/subnotes.py at master · scraggo/subnotes-python](https://github.com/scraggo/subnotes-python/blob/master/subnotes.py)

* [Anki Manual](https://apps.ankiweb.net/docs/manual.html)

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

def test_block_encoder():
    global ORG_LINKS
    text = ORG_LINKS
    app = App(text)
    pprint(app.encoded_list)

def test_return_sorted():
    global ORG_LINKS
    text = ORG_LINKS
    app = App(text)
    print(app.return_sorted())

def test_main():
    main()

def run_tests():
    # test_block_encoder()
    # test_return_sorted()
    test_main()

run_tests()