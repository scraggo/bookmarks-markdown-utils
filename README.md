# Bookmarks Project

Suite of command-line tools for Chrome bookmark management. (There is some functionality for OneTab and FireFox.) Designed for users who:

- Are tired of managing a large bookmark collection inside of Chrome.
- Use Chrome for both Desktop and Mobile bookmarking (and mainly use the "Mobile Bookmarks" folder)
- Want to convert bookmarks into individual markdown files
- Want a way to visit a site and tag the bookmark with minimal mouse movement
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
}

filenames = {
  'chr_md_file_prefix': {{ STRING - ex: 'chrome.md' }},
}

node_scripts = {
  'deleteLeadingText': {{ PATH TO deleteLeadingText }}
}
```

## chrome-to-markdown

Purpose:

- Backup Chrome 'Bookmarks' file to directory in config file.
- Convert file to markdown format.
- Copy mobile bookmarks to separate file.

## deleteLeadingText


## find_replace

**Necessary: Create the following configuration file:**
'config.json':
```
{
  "inputFile": {{ FILE TO PROCESS }},
  "outputDir": {{ OUTPUT DIRECTORY }},
  "firefoxJson": { see below }
}
```

Firefox JSON file location (Mac): "~/Library/Application Support/Google/Chrome/Default/Bookmarks"