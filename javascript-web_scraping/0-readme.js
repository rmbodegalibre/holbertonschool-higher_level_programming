#!/usr/bin/node
// This script reads and prints the content of a file.
// The first argument is the file path
// The content of the file is read in utf - 8
// If an error occurred during the reading, print the error object
const myFile = require('fs');

myFile.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
