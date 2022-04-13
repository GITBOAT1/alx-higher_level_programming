#!/usr/bin/node
/** Write a script that reads and prints the content of a file. */

const fs = require('fs');
const myArgs = process.argv.slice(2);

fs.readFile(myArgs[0], function (err, data) {
  if (err) {
    return console.error(err);
  }
  console.log(data.toString());
});
