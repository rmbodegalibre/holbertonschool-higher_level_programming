#!/usr/bin/node
// print process.argv
let numArgs = process.argv.length;
console.log(numArgs === 2 ? 'No argument' : numArgs === 3 ? 'Argument found' : 'Arguments found');
