#!/usr/bin/node
// print process.argv
const numArgs = process.argv.length;
console.log(numArgs === 2 ? 'No argument' : numArgs === 3 ? 'Argument found' : 'Arguments found');
