#!/usr/bin/node
/** Write a script that reads and prints the content of a file. */

const fs = require('request');
const myArgs = process.argv.slice(2);

fs(myArgs[0], function (err, data, body) {
  if (err) {
    return console.error(err);
  }
	fil = JSON.parse(body)
	console.log(typeof(fil.results), Object.keys(fil.results).length);
});
