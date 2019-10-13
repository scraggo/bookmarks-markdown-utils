import os
import sys
import json

userHome = os.path.expanduser('~')
config_name = 'config.json'

config_template = {
    "directories": {
        "bookmarksRootDir": os.path.join(userHome, 'Desktop', 'bookmarksBackups'),
        "chromeJSON": os.path.join("chrome_json"),
        "chromeMD": os.path.join("chrome_md"),
        "firefoxJson": os.path.join(
            userHome, "Library/Application Support/Google/Chrome/Default/Bookmarks"),
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
