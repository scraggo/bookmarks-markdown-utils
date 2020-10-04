#pythontemplate
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 4/26/17, 11:18 AM

@author: davecohen

Title: Convert Firefox Backup (JSON) to Markdown Links

Example input:
{
   "checksum": "fff",
   "roots": {
      "bookmark_bar": {
         "children": [ {
            "date_added": "131313",
            "id": "3462",
            "name": "Bookmarks",
            "sync_transaction_version": "2904",
            "type": "url",
            "url": "chrome://bookmarks/"
         }, {
            "children": [ {
               "children": [ {
                  "date_added": "13074",
                  "id": "215",
                  "meta_info": {
                     "last_visited_desktop": "13143530495705006"
                  },
                  "name": "Investing - Google Sheets",
                  "sync_transaction_version": "1",
                  "type": "url",
                  "url": "https://docs.google.com/spreadsheets/"
               }, {
                  "date_added": "130803232",
                  "id": "314",
                  "name": "Wunderlist",
                  "sync_transaction_version": "1",
                  "type": "url",
                  "url": "https://www.wunderlist.com/#/lists/inbox"
               }
             ]
          }
        ]
     }
   },
   "version": 1
}
"""

import os, sys, re, json
import pyperclip

def create_file(outputlocation, write_mode, textfile, replace_func):
    with open(outputlocation, write_mode) as output:
      with open(textfile, 'r') as f:
          for line in f:
              line = line.strip()
              line = replace_func(line)
              output.write(line)
    print('Output to:', outputlocation)

def replacer(arr, str):
  """Given list 'arr' of modifications,
  return str with specified modifications.
  params:
    arr: list of lists [string to find, string to replace with]
    str: string
  Caution - watch out for unicode chars. Ex: ' ' is unicode \xa0
    (this seems to only occur when replacers are tuples)
  """
  for item in arr:
    str = str.replace(item[0], item[1])
  return str

def get_replaced_line(line):
    '''This function is file-specific
    '''
    to_delete = [
        ['"type": "url",', '']
    ]

    to_replace_name = [
        ['"name": "', '* ['],
        ['",', ']']
    ]

    to_replace_paren = [
        ['(', '['],
        [')', ']']
    ]

    line = replacer(to_delete, line)
    if line.startswith('"name"'):
        return replacer(to_replace_name, line)
    elif line.startswith('"url"'):
        if 'chrome-extension://' in line:
            line = re.sub(r"chrome-extension://([a-z])+/suspended.html#uri=", "", line)
        line = line.replace('"url": "', '(')
        line_paren = line.replace('"', ')')
        line = line_paren + ' | ' + replacer(to_replace_paren, line_paren) + line_paren
        return line + '\n'
    return ''

def main():
    # get path to file
    config = pyperclip.paste()
    # load firefox json file
    with open(config, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())

    ff_json_list = str(data).split(', ')

    output_filename = 'firefox_output.html'

    # put in same directory as config
    outputlocation = config.split('/')[0:-2] + '/' + output_filename

    if os.path.exists(outputlocation):
      sys.exit('Error saving file.')

    create_file(outputlocation, 'w', ff_json_list, get_replaced_line)

if __name__ == '__main__':
    main()
