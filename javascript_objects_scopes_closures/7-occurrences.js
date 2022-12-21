#!/usr/bin/node
// This script contains a function that returns the number of occurrences in a list:
exports.nbOccurences = function (list, searchElement) {
  list = list.filter(element => element === searchElement);
  return list.length;
}
