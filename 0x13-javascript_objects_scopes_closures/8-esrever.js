#!/usr/bin/node
/**
 * a function that returns the reversed version of a list:
 * Prototype: exports.esrever = function (list)
 **/
exports.esrever = function (list) {
  let result = [];

  for (let i = list.length - 1; i >= 0; i--) {
    result.push(list[i]);
  }

  return (result);
};
