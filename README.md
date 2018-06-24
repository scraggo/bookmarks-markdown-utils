# Bookmarks to Markdown Utilities

Collection of command-line tools for Chrome bookmark management. (There is some functionality for OneTab, Evernote, and FireFox.) Designed for users who:

- dislike managing a large bookmark collection inside of Chrome.
- use Chrome for both Desktop and Mobile bookmarking (and mainly use the "Mobile Bookmarks" folder)
- want to convert bookmarks into individual markdown files
- want a way to visit a site and tag the bookmark with minimal mouse movement
- ...and more

Note: the configuration file needs to be created with the instructions below:

- `cd setup/`
- `python setup.py`
- `open ../config.json` to open file for editing.
- (Optional) Replace given directories with your own.

```
directories = {
  "bookmarksRootDir": {{ ROOT DIRECTORY }},
  "mobileLinksDir": {{ DIRECTORY INSIDE ROOT DIRECTORY or '' }},
  "markdownBackupsDir": {{ DIRECTORY INSIDE ROOT DIRECTORY or '' }},
  "chrJsonBackupsDir": {{ DIRECTORY INSIDE ROOT DIRECTORY or '' }},
  "combinedFiles": {{ DIRECTORY INSIDE ROOT DIRECTORY  or '' }}
  "firefoxJson": {{ *LOCATION OF FIREFOX JSON FILE }}
}

filenames = {
  'chr_md_file_prefix': {{ STRING - ex: 'chrome.md' }},
}

node_scripts = {
  'deleteLeadingText': {{ PATH TO deleteLeadingText }}
}
```

\* Firefox JSON file location (Mac): "~/Library/Application Support/Google/Chrome/Default/Bookmarks"

# Using the scripts

This is entirely written in Python 3+. Non-standard modules include:

- pyperclip
- pytest (for running tests)

## chrome-to-markdown

Purpose:

- Backup Chrome 'Bookmarks' file to directory in config file.
- Convert file to markdown format.
- Copy mobile bookmarks to separate file.
- You may delete the bookmarks in your Chrome mobile bookmarks folder afterwards.

`cd chrome-to-markdown`

`python main.py`

## deleteLeadingText


## find_replace

