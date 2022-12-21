#!/usr/bin/node
// This script contains a class Rectangle that defines a rectangle:
// This script uses the class notation for defining your class
// The constructor takes 2 arguments w and h
// This initializes the instance attribute width with the value of w
// This initializes the instance attribute height with the value of h
// If w or h is equal to 0 or not a positive integer, create an empty object
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
