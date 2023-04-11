#!/usr/bin/node
// A script that prints the addition of 2 integers

function add (a, b) {
  return a + b;
}

const argA = parseInt(process.argv[2]);
const argB = parseInt(process.argv[3]);
if (isNaN(argA) || isNaN(argB)) {
  console.log('NaN');
} else {
  console.log(add(argA, argB));
}
