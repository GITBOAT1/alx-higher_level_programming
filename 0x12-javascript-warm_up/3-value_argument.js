#!/usr/bin/node
/**
 * "argv and argc”
 *
 */
const args = process.argv
if (args[2] != null) {
  console.log(args[2])
} else if (args[2] == null) {
  console.log('No argument')
}
