#!/usr/bin/node
/**
 * "argv and argc”
 *
 */
const args = process.argv
if (args[2] != null) {
  console.log('No argument')
} else {
  console.log('Argument found')
}
