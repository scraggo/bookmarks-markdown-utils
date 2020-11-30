import os
import sys
import json

userHome = os.path.expanduser('~')
config_name = 'config.json'
bookmarks_root = os.path.join(userHome, 'Desktop', 'bookmarksBackups'),

config_template = {
    "directories": {
        "bookmarksRootDir": bookmarks_root,
        "chromeJSON": os.path.join(bookmarks_root, "chrome_json"),
        "chromeMD": os.path.join(bookmarks_root, "chrome_md"),
        "combinedFiles": "combined",
        "firefoxHTML": os.path.join(bookmarks_root, 'firefox_html'),
        "firefoxMD": os.path.join(bookmarks_root, 'firefox_md'),
        "mobileLinksDir": "mobileLinks",
    },

    "filenames": {
        "chr_md_file_prefix": "chrome.md"
    },

    "markdownFormat": "standard"
}


def write_config_file(new_filename):
    with open(new_filename, 'w') as new_file:
        new_file.write(
            json.dumps(config_template, indent=4)
        )
    print('File successfully written:', new_filename)


def file_exists(filePath):
    if os.path.exists(filePath):
        raise OSError(filePath + ' file exists.')


def main():
    config_main_directory = os.path.join('..', config_name)
    file_exists(config_main_directory)
    write_config_file(config_main_directory)


if __name__ == "__main__":
    main()
