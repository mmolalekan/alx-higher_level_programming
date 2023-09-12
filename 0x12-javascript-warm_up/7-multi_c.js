#!/usr/bin/node

const argv = process.argv;
if (!argv[2] || isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = parseInt(argv[2]); i > 0; i--) {
    console.log('C is fun');
  }
}
