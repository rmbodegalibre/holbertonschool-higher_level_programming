#!/usr/bin/node
// This script contains a class Square that defines a square and inherits from Square of 5-square.js:
// It uses the class notation for defining the class and extends
// It contains an instance method called charPrint(c) that prints the rectangle using the character c
// If c is undefined, use the character X
class Square extends require('./5-square') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
