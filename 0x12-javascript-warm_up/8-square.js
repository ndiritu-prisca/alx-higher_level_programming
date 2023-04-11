#!/usr/bin/node
// A script that prints a square

const arg = parseInt(process.argv[2]);
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let row = 0; row < arg; row++) {
    console.log('X'.repeat(arg));
  }
}
