# Bookmarks Project

Suite of command-line tools for Chrome bookmark management. Designed for users who want to store bookmark files in markdown format instead of managing a large collection inside of Chrome.

Note: the configuration files are not included. They can be created with the schema below.

## DEC-Chr2Markdown

Purpose:
- Backup Chrome 'Bookmarks' file to directory in config file.
- Convert file to markdown format.

**Necessary: Create the following configuration file:**
'chr_config.py':
```
directories = {
  "bookmarksRootDir": {{ ROOT DIRECTORY }},
  "mobileLinksDir": {{ DIRECTORY INSIDE ROOT DIRECTORY }},
  "markdownBackupsDir": {{ DIRECTORY INSIDE ROOT DIRECTORY }},
  "chrJsonBackupsDir": {{ DIRECTORY INSIDE ROOT DIRECTORY }},
}

filenames = {
  'chr_md_file_prefix': {{ STRING - ex: 'chrome.md' }},
}

node_scripts = {
  'deleteLeadingText': {{ PATH TO deleteLeadingText }}
}
```

## deleteLeadingText

**Necessary: Create the following configuration file:**
'config.json':
```
{
  "bookmarksRootDir": {{ ROOT DIRECTORY }},
  "mobileLinksDir": {{ DIRECTORY INSIDE ROOT DIRECTORY }},
  "markdownBackupsDir": {{ DIRECTORY INSIDE ROOT DIRECTORY }},
  "chrJsonBackupsDir": {{ DIRECTORY INSIDE ROOT DIRECTORY }},
}
```

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