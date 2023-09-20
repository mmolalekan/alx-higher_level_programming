#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
// super class constructor takes charge here.
  charPrint (C) {
    if (C === 'C') {
      for (let i = 0; i < this.height; i++) {
        console.log('C'.repeat(this.height));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
