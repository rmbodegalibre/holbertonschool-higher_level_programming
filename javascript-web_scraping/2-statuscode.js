#!/usr/bin/node
// This script displays the status code of a GET request.
// The first argument is the URL to request (GET)
// The status code is printed like this: code: <status code>
// It uses the module request
const reqStatus = require('request');
reqStatus.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
