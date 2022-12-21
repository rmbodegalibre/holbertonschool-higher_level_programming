#!/usr/bin/node
// This script contains a function that prints the number of arguments already printed and the new argument value.
// Output format: <number arguments already printed>: <current argument value>
let sequence = 0;
exports.logMe = function (item) {
  console.log(sequence++ + ': ' + item);
};
