import os
import subprocess
import sys

# "scriptName": [ "path", "fileName" ]
argPathMap = {
    'chrome_to_markdown': ['chrome_to_markdown', 'main.py'],
    'combine_files': ['combine_files', 'combine_files.py'],
    'delete_leading_text': ['delete_leading_text', 'delete_leading_text.py'],
    'find_replace_chrome_html': ['find_replace', 'find_replace_chrome_html.py'],
    'find_replace_evernote_html': ['find_replace', 'find_replace_evernote_html.py'],
    'find_replaceJSON_FF_01': ['find_replace', 'find_replaceJSON_FF_01.py'],
    'find_replaceJSON_FF_02': ['find_replace', 'find_replaceJSON_FF_02.py'],
    'firefox_html_to_markdown': ['find_replace', 'firefox_html_to_markdown.py'],
    'makelink_evernote_md': ['make_link', 'makelink_evernote_md.py'],
    'makelink_url': ['make_link', 'makelink_url.py'],
    'onetab_to_markdown': ['onetab_to_markdown', 'onetab_to_markdown.py'],
    'org_tagged_md_links': ['org_tagged_md_links', 'org_tagged_md_links.py'],
    'setup': ['setup', 'setup.py'],
    'visit_and_tag_md_links': ['visit_and_tag_md_links', 'main.py']
}

help_text = 'Valid scripts are:\n   ' + \
    "\n   ".join(map(lambda x: "'" + x + "'", argPathMap.keys()))


def show_help_and_exit(help=help_text):
    print(help)
    sys.exit()


def show_help_if_arg(args, helpText):
    if len(args) > 1 and args[1] == '-h':
        show_help_and_exit(helpText)


def handle_no_match(val0=None):
    if val0 == None:
        print('Script not found.')
        show_help_and_exit()


def safe_get_path(key):
    values = argPathMap.get(key, [None, None])
    handle_no_match(values[0])
    return values


def get_rest_of_args(args, startIdx=0):
    if len(args) < startIdx + 1:
        return []
    return args[startIdx:]


def execute_args(args):
    '''assuming args[0] is script name...'''
    if len(args) < 1:
        handle_no_match()
    if args[0] == '-h':
        show_help_and_exit()

    scriptName = args[0]
    path, fileName = safe_get_path(scriptName)
    restOfArgs = get_rest_of_args(args, 1)

    os.chdir(path)
    subprocess.run(
        ['python', fileName] + restOfArgs)
