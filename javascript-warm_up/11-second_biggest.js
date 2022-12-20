#!/usr/bin/node
// This script searches the second biggest integer in the list of arguments.
// We can assume all arguments can be converted to integer
// If no argument passed, print 0
// If the number of arguments is 1, print 0
if (process.argv.length > 3) {
  const myArgs = process.argv.slice(2, process.argv.length).map(Number);
  myArgs.sort((a, b) => a - b);
  console.log(myArgs[myArgs.length - 2]);
} else {
  console.log(0);
}
