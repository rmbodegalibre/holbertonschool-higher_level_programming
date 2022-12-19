#!/usr/bin/node
// print process.argv
let num_args = process.argv.length;
console.log(num_args === 2 ? 'No argument' : num_args === 3 ? 'Argument found' : 'Arguments found');
