#!/usr/bin/node
/**
 * "Write a script that prints My number: <first argument
 * converted in integer> if the first argument can be converted to an integer”
 *
 */

const num = process.argv[2]
if (Number(num)) {
  console.log('My number: ' + num)
} else {
  console.log('Not a number')
}
