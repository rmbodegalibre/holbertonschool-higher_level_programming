#!/usr/bin/node
// This script computes and prints a factorial
// The first argument is integer (argument can be cast as integer) used for computing the factorial
// Factorial of NaN is 1
// It does it recursively
// It use a function
function fact (myVar) {
  return myVar === 0 || isNaN(myVar) ? 1 : myVar * fact(myVar - 1);
}

console.log(fact(Math.floor(Number(process.argv[2]))));
