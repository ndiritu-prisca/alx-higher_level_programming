#!/usr/bin/node
// A script that computes and prints a factorial

function myFactorial (num) {
  if (isNaN(num) || num < 2) {
    return 1;
  } else {
    return (num * myFactorial(num - 1));
  }
}

console.log(myFactorial(process.argv[2]));
