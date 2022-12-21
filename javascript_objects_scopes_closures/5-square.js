#!/usr/bin/node
// This script contains a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:
// It uses the class notation for defining your class and extends
// The constructor takes 1 argument: size
// The constructor of Rectangle id called (by using super()
class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
