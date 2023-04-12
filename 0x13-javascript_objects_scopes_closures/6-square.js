#!/usr/bin/node
const Square0 = require('./5-square');

class Square extends Square0 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let x = 0; x < this.height; x++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}

module.exports = Square;
