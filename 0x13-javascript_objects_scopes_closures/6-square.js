#!/usr/bin/node
const Squares = require('./5-square.js');
module.exports = class Square extends Squares {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.height));
    }
  }
};
