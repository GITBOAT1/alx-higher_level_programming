#!/usr/bin/node
/**
 * Write a function that returns the number of occurrences in a list:
 * Prototype: exports.nbOccurences = function (list, searchElement)
 **/
'use strict';
exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;

  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      occurences += 1;
    }
  }
  return (occurences);
};
