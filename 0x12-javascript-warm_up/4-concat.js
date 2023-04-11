#!/usr/bin/node
// A script that prints two arguments passed to it, in the following format:
// “ is ”

const args = process.argv;
const numArgs = args.length;
if (numArgs === 2) {
  console.log('undefined is undefined');
} else if (numArgs === 3) {
  console.log(args[2] + ' is undefined');
} else {
  console.log(args[2] + ' is ' + args[3]);
}
