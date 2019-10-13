import os
import sys

# this import only works if you're in this directory
sys.path.insert(0, '../utils')
from get_config import get_json_config

dirs = get_json_config()['directories']

constants = {
    'title': '## MOBILE BOOKMARKS',
    'outputMessage': 'Successfully made a copy of your mobile bookmarks folder as markdown. Output to: ',
    'extension': '-mobile.md'
}

description = '''error: expected inputFilename

Usage:
Command line: python delete_leading_text.py inputFilename [Optional: output path]

This script is called after chrome-to-markdown. It copies the markdown file to a new directory and removes all the text above `## MOBILE BOOKMARKS`.
'''

if len(sys.argv) < 2:
    sys.exit(description)

inputFilePath = sys.argv[1]

outputFilePath = os.path.join(dirs['bookmarksRootDir'], dirs['mobileLinksDir'])

# optional output path:
if len(sys.argv) > 2:
    outputFilePath = sys.argv[2]

date = inputFilePath[-9:-3]  # get date
outputFilename = date + constants['extension']
fullOutputPath = os.path.join(outputFilePath, outputFilename)

if os.path.exists(fullOutputPath):
    sys.exit('File exists: ' + fullOutputPath)


def writeToFile():
    with open(fullOutputPath, 'w') as outfile:
        found = False
        with open(inputFilePath, 'r') as infile:
            for line in infile:
                if constants['title'] in line:
                    found = True
                if found:
                    outfile.write(line.strip() + '\n')


writeToFile()
print(constants['outputMessage'] + fullOutputPath)
