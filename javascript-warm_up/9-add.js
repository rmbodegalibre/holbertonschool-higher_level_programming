#!/usr/bin/node
// This script prints the addition of two integers
// The first argument is the first integer
// The second argument is the second integer
// It defines a function with this prototype: function add(a, b)
function sum(a, b) {
  return a + b;
}

console.log(sum(Math.floor(Number(process.argv[2])), Math.floor(Number(process.argv[3]))));
