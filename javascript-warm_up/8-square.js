#!/usr/bin/node
// This script prints a square
// The first argument is the size of the square
// If the first argument can’t be converted to an integer, print “Missing size”
// It uses the character X to print the square
// It uses a loop (while, for, etc.)
const myVar = Math.floor(Number(process.argv[2]));
if (!isNaN(myVar)) {
  for (let i = 0; i < myVar; i++) {
    console.log('X'.repeat(myVar));
  }
} else {
  console.log('Missing size');
}
