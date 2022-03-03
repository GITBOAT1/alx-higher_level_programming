#!/usr/bin/node
/**
* Write a script that imports a dictionary of occurrences 
* by user id and computes a dictionary of user ids by occurrence.
**/
const dict = require('./101-data.js').dict;

let newDict = {};

for (let key in dict) {
  newDict[dict[key]] = [];
}

for (let key in dict) {
  newDict[dict[key]].push(key);
}

console.log(newDict);
