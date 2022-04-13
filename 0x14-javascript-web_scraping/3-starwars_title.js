#!/usr/bin/node
/** Write a script that reads and prints the content of a file. */

const fs = require('request');
const myArgs = process.argv.slice(2);
const url = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0];
fs(url, function (err, data, body) {
  if (err) {
    return console.error(err);
  }
  const str = JSON.parse(body);
  console.log(str.title);
});
