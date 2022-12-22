#!/usr/bin/node
// This script a string to a file.
// The first argument is the file path
// The second argument is the string to write
// The content of the file is written in utf-8
// If an error occurred during the writting, print the error object
const myFile = require('fs');
const content = process.argv[3];

try {
  myFile.writeFileSync(process.argv[2], content);
} catch (err) {
  console.error(err);
}
