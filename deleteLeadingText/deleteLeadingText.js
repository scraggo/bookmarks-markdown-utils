/*
In a new file, only include `## MOBILE BOOKMARKS` and text afterwards.

Usage:
Command line: node scriptName fileWithAllLinks [Optional: output destination]
*/

const fs = require('fs');
const path = require('path');

const {bookmarksRootDir, mobileLinksDir} = require('./config.json');

const config = {
  title: '## MOBILE BOOKMARKS',
  outputFilePath: path.join(bookmarksRootDir, mobileLinksDir),
  outputMessage: 'Your file has been written: ',
  extension: '-mobile.md'
};

const inputFilePath = process.argv[2];

// optional:
const outputFilePath = process.argv[3] || config.outputFilePath;

const dateAndExtension = inputFilePath.slice(-9);
const outputFilename = dateAndExtension.slice(0, 6) + config.extension;
const fullOutputPath = path.join(outputFilePath, outputFilename);

// console.log(outputFilename, outputFilePath);

if (fs.existsSync(fullOutputPath)) {
  throw Error('File exists: ' + fullOutputPath);
}

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

// Promise.resolve(writeToFile()).then(() => {
//   console.log('\n\n' + config.outputMessage + fullOutputPath);
// }).catch(console.error);

writeToFile();
console.log('\n\n' + config.outputMessage + fullOutputPath);

