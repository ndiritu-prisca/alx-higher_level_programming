#!/usr/bin/node
// A function that increments and calls a function.

exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
