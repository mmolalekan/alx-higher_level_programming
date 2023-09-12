#!/usr/bin/node

function recursion (a) {
  if (a > 0) {
    return a * recursion(a - 1);
  } else {
    return 1;
  }
}

const argv = process.argv[2];
if (!argv || isNaN(argv)) {
  console.log('1');
} else {
  const result = recursion(parseInt(argv));
  console.log(`${result}`);
}
