"""Long Format
- [name](url) | [url](url)

example:
- [America’s most popular voting guide for elections, political issues, candidates, and poll data](https://www.isidewith.com/) | [https://www.isidewith.com/](https://www.isidewith.com/)
"""


def handle_long_name(line):
    return line\
        .replace('"name": "', '- [')\
        .replace('",', ']')


def handle_long_url(line):
    line = line.replace('"url": "', '(')
    line_paren = line.replace('"', ')')
    return line_paren + ' | ' + \
        line_paren.replace(
            '(', '[').replace(')', ']') + line_paren


"""Short Format
- name <url>

example:

- Google Search <http://google.com>
"""


def handle_short_name(line):
    return line\
        .replace('"name": "', '- ')\
        .replace('",', ' ')


def handle_short_url(line):
    return line\
        .replace('"url": "', '<')\
        .replace('"', '>')


"""Standard Format
- [name](url)

example:

- [Google Search](http://google.com)
"""


def handle_standard_name(line):
    return line\
        .replace('"name": "', '- [')\
        .replace('",', ']')


def handle_standard_url(line):
    return line\
        .replace('"url": "', '(')\
        .replace('"', ')')


markdownFormatMap = {
    "long": {
        "name": handle_long_name,
        "url": handle_long_url
    },
    "short": {
        "name": handle_short_name,
        "url": handle_short_url
    },
    "standard": {
        "name": handle_standard_name,
        "url": handle_standard_url
    },
}
