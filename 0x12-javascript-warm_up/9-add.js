#!/usr/bin/node
/**
 *
 * Write a script that prints the addition of 2 integers
 */
function add (a, b) {
  return (a + b)
}
const pro = Number(process.argv[2])
const pro2 = Number(process.argv[3])
console.log(add(pro, pro2))
