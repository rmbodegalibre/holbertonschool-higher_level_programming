#!/usr/bin/node
// This script gets the contents of a webpage and stores it in a file.
// The first argument is the URL to request
// The second argument the file path to store the body response
// The file is UTF - 8 encoded
// It uses the module request
const myFile = require('fs');
const reqContent = require('request');
reqContent(process.argv[2]).pipe(myFile.createWriteStream(process.argv[3]));
