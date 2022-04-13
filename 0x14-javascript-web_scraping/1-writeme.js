#!/usr/bin/node
/** Write a script that write the content to a file. */

const fs = require('fs');
const myArgs = process.argv.slice(2);

fs.writeFile(myArgs[0], myArgs[1], function (err) {
  if (err) {
    return console.error(err);
  }
});
