#!/usr/bin/node
// A script that prints a message depending of the number of arguments passed

const args = process.argv;
const numArgs = args.length;
if (numArgs === 2) {
  console.log('No argument');
} else if (numArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
