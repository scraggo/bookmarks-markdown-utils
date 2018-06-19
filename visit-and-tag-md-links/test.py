#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from link_org_nospace import *

todoTxt = \
'''
* [Mobile-Keep]* [Other Bookmarks]* [---MOBILE-BOOKMARKS](about:blank) | [about:blank](about:blank)
* [When am I experienced enough to apply for internships?](https://www.reddit.com/r/cscareerquestions/comments/6o3he4/when_am_i_experienced_enough_to_apply_for/) | [https://www.reddit.com/r/cscareerquestions/comments/6o3he4/when_am_i_experienced_enough_to_apply_for/](https://www.reddit.com/r/cscareerquestions/comments/6o3he4/when_am_i_experienced_enough_to_apply_for/)
* [What are you guys using for styling form controls nowadays?](https://www.reddit.com/r/web_design/comments/6pphww/what_are_you_guys_using_for_styling_form_controls/) | [https://www.reddit.com/r/web_design/comments/6pphww/what_are_you_guys_using_for_styling_form_controls/](https://www.reddit.com/r/web_design/comments/6pphww/what_are_you_guys_using_for_styling_form_controls/)
* [O'Reilly is offering ebooks about UX, Data, IoT...](https://www.reddit.com/r/webdev/comments/6pgjg4/oreilly_is_offering_ebooks_about_ux_data_iot/) | [https://www.reddit.com/r/webdev/comments/6pgjg4/oreilly_is_offering_ebooks_about_ux_data_iot/](https://www.reddit.com/r/webdev/comments/6pgjg4/oreilly_is_offering_ebooks_about_ux_data_iot/)
* [SPAs vs MPAs/MVC - Are Single Page Apps always better?](https://www.reddit.com/r/webdev/comments/6phqhe/spas_vs_mpasmvc_are_single_page_apps_always_better/) | [https://www.reddit.com/r/webdev/comments/6phqhe/spas_vs_mpasmvc_are_single_page_apps_always_better/](https://www.reddit.com/r/webdev/comments/6phqhe/spas_vs_mpasmvc_are_single_page_apps_always_better/)
* [Rotten oranges problem, http://www.geeksforgeeks.org/minimum-time-required-so-that-all-oranges-become-rotten/](https://www.reddit.com/r/Python/comments/6vk31h/rotten_oranges_problem/) | [https://www.reddit.com/r/Python/comments/6vk31h/rotten_oranges_problem/](https://www.reddit.com/r/Python/comments/6vk31h/rotten_oranges_problem/)
'''

def test_visit_link():
    # global todoTxt
    t = todoTxt.split('\n')
    test = App(t)
    for line in t:
        print(line)
        test.visit_link(line)

def run_test_suite():
    test_visit_link()

run_test_suite()