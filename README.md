# Bookmarks to Markdown Utilities

Collection of command-line tools for Chrome bookmark management. (There is some functionality for OneTab, Evernote, and FireFox.) Designed for personal use and other users who may:

- dislike managing a large bookmark collection inside of Chrome.
- use Chrome for both Desktop and Mobile bookmarking (and mainly use the "Mobile Bookmarks" folder)
- want to convert bookmarks into individual markdown files
- want a way to visit a site and tag the bookmark with minimal mouse movement
- ...and more.

Note: the configuration file needs to be created with the instructions below:

- `cd setup/`
- `python setup.py`
- `open ../config.json` to open file for editing.
- (Optional) Replace given directories with your own. (see below)

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

```

\* Firefox JSON file location (Mac): "~/Library/Application Support/Google/Chrome/Default/Bookmarks"

### Using the scripts

This is entirely written in Python 3+. Non-standard modules include:

- pyperclip
- pytest (for running tests)

All files are run from the project root in the command line (terminal.app, iterm.app, etc.)

# chrome-to-markdown

Purpose:

- Backup Chrome 'Bookmarks' file to directory in config file.
- Convert file to markdown format.
- Copy mobile bookmarks to separate file. (this is a call to `delete_leading_text` - see below).
- You may delete the bookmarks in your Chrome mobile bookmarks folder afterwards.

```bash
# from project root:
cd chrome-to-markdown
python main.py
```

# combine_files

Purpose:

Given files of a specified type, their text is combined into one file.

```bash
# from project root:
cd combine_files
python combine_files.py [-h] # to see necessary arguments
```

# delete_leading_text

Purpose:

- Copy mobile bookmarks to separate file. It deletes all links before `# MOBILE BOOKMARKS`

```bash
# from project root:
cd delete_leading_text
python delete_leading_text.py <input file name> [output file name]
```


# find_replace

Purpose:

- Given a bookmarks html file (commonly used bookmarks backup format), after all styling and classes are removed, we're left with a "clean" html file. (Cleaning is not done inside this codebase.)
- There are multiple scripts that can be run depending on the format:
  1. `find_replace_chrome_html.py`
  2. `find_replace_evernote_html.py`
  3. `find_replaceJSON_FF_01.py` (Firefox)
  4. `find_replaceJSON_FF_02.py` (Firefox)
- The html will be converted to markdown.

```bash
# from project root:
cd find_replace
python find_replace_<scriptname> [*input file] [*output path]
```

\* Note: only 1 and 2 allow user to specify input and output paths. More documentation is inside the scripts. (<- Need to fix.)

# make_link

Purpose:

- Given links in a few formats (plain url, Evernote), the text will be converted to markdown. 
  1. `makelink_evernote_md.py`
  2. `makelink_url.py`
- More documentation is inside the scripts. (<- Need to fix.)
- Follow program instructions for copying text to clipboard.

```bash
# from project root:
cd make_link
python makelink_<scriptname>
```

# onetab_to_markdown

Purpose:

- Given links in OneTab format (the "Import/Export" option), the text will be converted to markdown. 
- More documentation is inside the scripts. (<- Need to fix.)
- Follow program instructions for copying text to clipboard.

```bash
# from project root:
cd onetab_to_markdown
python onetab_to_markdown.py
```

# org_tagged_md_links

Purpose:

- Given links in markdown format with "tags", the grouped text will be sorted alphabetically.
- More documentation is inside the scripts. (<- Need to fix.)
- Follow program instructions for copying text to clipboard.

```bash
# from project root:
cd org_tagged_md_links
python org_tagged_md_links.py
```

# visit_and_tag_md_links

Purpose:

Given links in markdown format (all links are in a markdown list, prefixed with '*'):

- each link is visited in your default browser,
- then you can "tag" the link in the terminal. (switching can be done with keyboard using CMD+TAB)
- output format from my markdown encoder

```bash
# from project root:
cd visit_and_tag_md_links
python main.py <input filepath>
```
