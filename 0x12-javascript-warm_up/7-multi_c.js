#!/usr/bin/node
/**
 *
 * Write a script that prints x times “C is fun”
 */
const c = 'C is fun'
const pro = process.argv[2]
if (Number(pro)) {
  for (let i = 0; i < Number(pro); i++) {
    console.log(c)
  }
} else {
  console.log('Missing number of occurrences')
}
