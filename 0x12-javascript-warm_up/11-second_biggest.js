#!/usr/bin/node
// A script that searches the second biggest integer in the list of arguments

const args = process.argv;
const numArgs = args.length;

if ((numArgs === 2) || (numArgs === 3)) {
  console.log(0);
} else {
  args.sort(function (x, y) {
    return (x - y);
  });
  const secBiggest = args[numArgs - 2];
  console.log(secBiggest);
}
