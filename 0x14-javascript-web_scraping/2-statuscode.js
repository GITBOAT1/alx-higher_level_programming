#!/usr/bin/node
/** Write a script that sataus codee. */

const fs = require('request');
const myArgs = process.argv.slice(2);

fs(myArgs[0], function (err, response) {
  if (err) {
    return console.error(err);
  }
  console.log('code:', response && response.statusCode);
});
