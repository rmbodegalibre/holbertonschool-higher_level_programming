#!/usr/bin/node
// This script contains a function that returns the reversed version of a list:
exports.esrever = function (list) {
  const reverseList = [];
  while (list.length) {
    reverseList.push(list.pop());
  }

  return reverseList;
};
