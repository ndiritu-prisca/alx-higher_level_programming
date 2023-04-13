#!/usr/bin/node

const list = require('./100-data').list;
const myList = list.map(function (element, index) {
  return element * index;
});

console.log(list);
console.log(myList);
