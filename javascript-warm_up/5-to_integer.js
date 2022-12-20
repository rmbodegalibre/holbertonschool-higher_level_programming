#!/usr/bin/node
// This script  prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer:
const number = Math.floor(Number(process.argv[2]));
console.log(!isNaN(number) ? 'My number: ' + number : 'Not a number');
