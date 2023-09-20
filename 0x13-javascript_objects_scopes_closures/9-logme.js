#!/usr/bin/node

let count = -1;
exports.logMe = function (item) {
  console.log(`${count = count + 1}: ${item}`);
};
