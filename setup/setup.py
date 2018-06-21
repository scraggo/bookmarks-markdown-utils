import os, sys, json

# this import only works if you're in this directory
sys.path.insert(0, '../utils')
import file_utils

fUtils = file_utils.FileUtils()

userHome = os.path.expanduser('~')
bookmarksRootDir = os.path.join(userHome, 'Desktop', 'bookmarksBackups')
mobileLinksDir = 'mobileLinks'
markdownBackupsDir = os.path.join("markdown-converted-full")
chrJsonBackupsDir = os.path.join("chrome-json")
deleteLeadingText = os.path.join("..","deleteLeadingText","deleteLeadingText.js")
config_name = 'config.json'

config_template = {
  "directories": {
    "bookmarksRootDir": bookmarksRootDir,
    "mobileLinksDir": mobileLinksDir,
    "markdownBackupsDir": markdownBackupsDir,
    "chrJsonBackupsDir": chrJsonBackupsDir
  },

  "filenames": {
    "chr_md_file_prefix": "chrome.md"
  },

  "node_scripts": {
    "deleteLeadingText": deleteLeadingText
  }
}

def write_config_file(new_filename):
  with open(new_filename, 'w') as new_file:
    new_file.write(
      json.dumps(config_template, indent=4)
    )
  print('File successfully written:', new_filename)


try:
  config_main_directory = os.path.join('..', config_name)
  fUtils.fileExists(config_main_directory)
  write_config_file(config_main_directory)
except:
  print('file already exists.')
