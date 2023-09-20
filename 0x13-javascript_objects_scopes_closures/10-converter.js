#!/usr/bin/node

exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};

// exports.converter = function (base) {
//   return num => num.toString(base);
// }
