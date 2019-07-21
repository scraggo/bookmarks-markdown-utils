# Bookmarks to Markdown Utilities

Collection of command-line tools for Chrome, OneTab, Evernote, and FireFox bookmark management. The tools are mostly to convert proprietary formats to markdown and organizing and add tags. Designed for personal use and other users who may:

- want to convert bookmarks from various formats into individual markdown files
- collect a lot of bookmarks, want to tag them, but dislike doing it in the browser
- use Chrome for both Desktop and Mobile bookmarking (and mainly use the "Mobile Bookmarks" folder)
- want a way to visit a site and tag the bookmark with minimal mouse movement
- ...and more.

Note: the configuration file needs to be created with the instructions below:

- start in root directory
- `python main.py setup`
  - This will raise an error if the file already exists.
- `open ./config.json` to open file for editing.
- (Optional) Replace given directories with your own. (see below)

```txt
{
  "directories": {
    "bookmarksRootDir": root directory,
    "chromeJSON": directory inside root directory or "",
    "chromeMD": directory inside root directory or "",
    "combinedFiles": directory inside root directory  or "",
    "mobileLinksDir": directory inside root directory or ""
    "firefoxHTML": location of your saved firefox html backup file,
    "markdownBackupsDir": directory inside root directory or "",
    "mobileLinksDir": directory inside root directory or ""
  },

  "filenames": {
    "chr_md_file_prefix": ex: "chrome.md",
  },

  "markdownFormat": **one of "short", "standard", "long"
}

```

Chrome JSON file is found automatically. The default Mac location: "~/Library/Application Support/Google/Chrome/Default/Bookmarks"

\*\* Formats:

```txt
long:
- [name](url) | [url](url)
- [Google Search](http://google.com) | [http://google.com](http://google.com)

short:
- name <url>
- Google Search <http://google.com>

standard:
- [name](url)
- [Google Search](http://google.com)
```

## Using the scripts

This is entirely written in Python 3+. Non-standard modules include:

- html2text
- pyperclip
- pytest (for running tests)

Below are descriptions of each folder with relevant scripts and instructions for running the scripts. The instructions assume you are in the project root in your command line app of choice (terminal.app, iterm.app, etc.).

### chrome_to_markdown

- Backup Chrome 'Bookmarks' file to directory in config file.
- Convert file to markdown format.
- Copy mobile bookmarks to separate file. (this is a call to `delete_leading_text` - see below).
- You may delete the bookmarks in your Chrome mobile bookmarks folder afterwards.
- **Credit for part of this script goes to** [DavidMetcalfe/Chrome-Bookmarks-Parser: Back up and parse Google Chrome's Bookmarks.bak file](https://github.com/DavidMetcalfe/Chrome-Bookmarks-Parser).

Usage:

```bash
# from project root:
python main.py chrome_to_markdown
```

### combine_files

Given files of a specified type, their text is combined into one file.

Usage:

```bash
# from project root:
python main.py combine_files [-h] # (help) see necessary arguments
```

### delete_leading_text

- Copy mobile bookmarks to separate file. It deletes all links before `# MOBILE BOOKMARKS`
- (Note: this script is called inside `main.py` of "chrome_to_markdown")

Usage:

```bash
# from project root:
python main.py delete_leading_text <input file name> [output file name]
```

### find_replace

- Given a bookmarks html file (commonly used bookmarks backup format), after all styling and classes are removed, we're left with a "clean" html file. (Cleaning is not done inside this codebase.)
- There are multiple scripts that can be run depending on the format:

  1. `find_replace_chrome_html.py`
  2. `find_replace_evernote_html.py`
  3. `find_replaceJSON_FF_01.py` (Firefox) <- deprecated
  4. `find_replaceJSON_FF_02.py` (Firefox) <- deprecated
  5. `firefox_html_to_markdown` (Firefox) <- in progress. No "cleaning" necessary!

- The html will be converted to markdown.

Usage:

```bash
# from project root:
python main.py find_replace_<scriptname> [*input file] [*output path]
```

\* Note: only scripts 1 and 2 allow user to specify input and output paths. More documentation is inside the scripts. (<- to fix.)

### make_link

- Given links in a few formats (plain url, Evernote), the text will be converted to markdown.

  1. `makelink_evernote_md.py`
  2. `makelink_url.py`

- Follow program instructions for copying text to clipboard.

Usage:

```bash
# from project root:
python main.py makelink_<scriptname> [-h] # (help) more info
```

### onetab_to_markdown

- Given links in OneTab format (the "Import/Export" option), the text will be converted to markdown.
- Follow program instructions for copying text to clipboard.

Usage:

```bash
# from project root:
python main.py onetab_to_markdown [-h] # (help) more info
```

### org_tagged_md_links

- Given links in markdown format with "tags", the grouped text will be sorted alphabetically.
- Follow program instructions for copying text to clipboard.

Usage:

```bash
# from project root:
python main.py org_tagged_md_links [-h] # (help) more info
```

### visit_and_tag_md_links

Given links in markdown format (all links are in a markdown list, prefixed with '\*'):

- each link is visited in your default browser,
- then you can "tag" the link in the terminal. (switching can be done with keyboard using CMD+TAB)
- output format from my markdown encoder

Usage:

```bash
# from project root:
python main.py visit_and_tag_md_links <input filepath>
```
