/*
In a new file, only include `## MOBILE BOOKMARKS` and text afterwards.

Usage:
Command line: node scriptName fileWithAllLinks [Optional: output destination]
*/

const fs = require('fs');
const path = require('path');

const config = {
  title: '## MOBILE BOOKMARKS',
  outputFilePath: '/Users/davecohen/Dropbox/Notes/Programming-DB/-BookmarkProject/-Links-Private/MobileLinks',
  outputMessage: 'Your file has been written: '
};

const inputFilePath = process.argv[2];

// optional:
const outputFilePath = process.argv[3] || config.outputFilePath;

const dateAndExtension = inputFilePath.slice(-9);
const outputFilename = dateAndExtension.slice(0, 6) + '-mobile.md';
const fullOutputPath = path.join(outputFilePath, outputFilename);

// console.log(outputFilename, outputFilePath);

const writeToFile = () => {
  let found = false;
  fs.readFileSync(inputFilePath).toString().split('\n')
  .forEach((line) => {
    if (line.indexOf(config.title) > -1) found = true;
    if (found) {
      fs.appendFileSync(fullOutputPath, line.toString() + '\n');
    }
  });
};

Promise.resolve(writeToFile()).then(() => {
  console.log('\n\n' + config.outputMessage + fullOutputPath);
}).catch(console.error);
