
import os, sys, json
from visit_and_tag_md_links import App

# this import only works if you're in this directory
sys.path.insert(0, '../utils')
import file_utils
from get_config import get_json_config

md_file = '/Users/davecohen/Dropbox/Notes/Programming-DB/-BookmarkProject/-Links-Private/MobileLinks/171018-mobile.md'

def debug(obj):
  # {name: data}
  for name in obj.keys():
    print('{}: {}'.format(name, obj[name]))

def get_file_arr(file_path):
  with open(file_path) as f:
    return f.readlines()

def get_timestamp():
  import time
  return str(int(time.time() * 100))

def get_new_filepath(old_file):
  import os
  filename, file_extension = os.path.splitext(old_file)
  new_filename = filename + get_timestamp() + file_extension
  # debug(
  #   {
  #     "filename": filename,
  #     "file_extension": file_extension,
  #     "new_filename": new_filename,
  #   }
  # )
  return new_filename

def write_sorted_file(new_filename, header_str, links_list):
  with open(new_filename, 'w') as new_file:
    new_file.write(header_str)
    for obj in links_list:
      new_file.write('\n\n' + obj['header'] + '\n')
      for line in obj['data']:
        new_file.write(line.strip() + '\n')
  print('File successfully written:', new_filename)

def main():
  global md_file
  if len(sys.argv) > 1:
    md_file = sys.argv[1]
  links = App(get_file_arr(md_file))
  links.block_encoder()
  headerList = links.get_sorted_headers(string = True)
  # allLinks = links.return_sorted(string = False)
  allLinks = links.header_list
  newFileName = get_new_filepath(md_file)
  # print(headerList)
  # print(allLinks)
  # print(newFileName)

  write_sorted_file(newFileName, headerList, allLinks)

if __name__ == '__main__':
  main()