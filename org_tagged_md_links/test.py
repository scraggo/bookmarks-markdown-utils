#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pprint import pprint
import org_tagged_md_links

ORG_LINKS = '''
# MOBILE LINKS
## 2017 - May and June

Priority 1: search !!!
Chrome Extension
Lots of JavaScript in here.

# 5/24/2017

* [Anki Manual](https://apps.ankiweb.net/docs/manual.html)

A cool looking app / similar to my idea
* [[macOS] Workspaces (beta) - an app that recreates working environment](https://www.reddit.com/r/webdev/comments/6ca3ts/macos_workspaces_beta_an_app_that_recreates/) | [https://www.reddit.com/r/webdev/comments/6ca3ts/macos_workspaces_beta_an_app_that_recreates/](https://www.reddit.com/r/webdev/comments/6ca3ts/macos_workspaces_beta_an_app_that_recreates/)

# 170531

Python / OOP
* [PyBites: Code Challenge 20 - Object Oriented Programming Fun - Review](http://pybit.es/codechallenge20_review.html) | [http://pybit.es/codechallenge20_review.html](http://pybit.es/codechallenge20_review.html)

JavaScript / FCC
* [If I finish all certificates on freeCodeCamp, how long will I have to wait to start working on a n… by Quincy Larson](https://www.quora.com/If-I-finish-all-certificates-on-freeCodeCamp-how-long-will-I-have-to-wait-to-start-working-on-a-nonprofit-project/answer/Quincy-Larson?share=8f15f623&srid=4tK5) | [https://www.quora.com/If-I-finish-all-certificates-on-freeCodeCamp-how-long-will-I-have-to-wait-to-start-working-on-a-nonprofit-project/answer/Quincy-Larson?share=8f15f623&srid=4tK5](https://www.quora.com/If-I-finish-all-certificates-on-freeCodeCamp-how-long-will-I-have-to-wait-to-start-working-on-a-nonprofit-project/answer/Quincy-Larson?share=8f15f623&srid=4tK5)

WebDev
* [“My path to web development”](https://www.reddit.com/r/learnprogramming/comments/6djovj/my_path_to_web_development/) | [https://www.reddit.com/r/learnprogramming/comments/6djovj/my_path_to_web_development/](https://www.reddit.com/r/learnprogramming/comments/6djovj/my_path_to_web_development/)

Regex resources
* [If you struggle with REGULAR EXPRESSIONS, here is an awesome site that helps you understand them really quickly](https://www.reddit.com/r/learnprogramming/comments/6d93fs/if_you_struggle_with_regular_expressions_here_is/) | [https://www.reddit.com/r/learnprogramming/comments/6d93fs/if_you_struggle_with_regular_expressions_here_is/](https://www.reddit.com/r/learnprogramming/comments/6d93fs/if_you_struggle_with_regular_expressions_here_is/)

Interesting reading.
* [Looking for most enjoyed non-Python languages used by Python developers](https://www.reddit.com/r/Python/comments/6d5yn3/looking_for_most_enjoyed_nonpython_languages_used/) | [https://www.reddit.com/r/Python/comments/6d5yn3/looking_for_most_enjoyed_nonpython_languages_used/](https://www.reddit.com/r/Python/comments/6d5yn3/looking_for_most_enjoyed_nonpython_languages_used/)
'''


def test_block_encoder():
    # global ORG_LINKS
    text = ORG_LINKS
    app = org_tagged_md_links.App(text)
    pprint(app.encoded_list)


def test_return_tags():
    # global ORG_LINKS
    text = ORG_LINKS
    app = org_tagged_md_links.App(text)
    print(app.returnTags())


def test_return_sorted():
    # global ORG_LINKS
    text = ORG_LINKS
    app = org_tagged_md_links.App(text)
    print(app.return_sorted())


def test_main():
    org_tagged_md_links.main()


def run_tests():
    # test_block_encoder()
    # test_return_tags()
    # test_return_sorted()
    test_main()


run_tests()
