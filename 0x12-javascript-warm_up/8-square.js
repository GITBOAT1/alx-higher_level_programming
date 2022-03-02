#!/usr/bin/node
/**
 *
 * Write a script that prints x times “C is fun”
 */
const c = 'X'
const pro = process.argv[2]
if (Number(pro)) {
  for (let i = 0; i < Number(pro); i++) {
    for (let j = 0; j < Number(pro); j++) {
      process.stdout.write(c)
    }
    console.log()
  }
} else {
  console.log('Missing size')
}
