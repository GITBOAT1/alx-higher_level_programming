#!/usr/bin/node
/**
 *
 * Write a script that prints the addition of 2 integers
 */
function add (a) {
  if (a < 0) {
    return (1)
  } else {
    return (a * (a - 1))
  }
}
const pro = process.argv[2]
if (Number(pro)) {
  console.log(add(pro))
} else {
  console.log(0)
}
