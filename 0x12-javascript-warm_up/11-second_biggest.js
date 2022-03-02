#!/usr/bin/node
/**
 *
 * Write a script that searches the second biggest integer in the list of arguments.
 */

const pro = process.argv[2]

let s = 0
for (let i = 2; i < process.argv.length; i++) {
  const l = Number(process.argv[i])
  if (l > s) {
    s = l
  }
}
console.log(s)
