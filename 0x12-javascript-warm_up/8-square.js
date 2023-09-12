#!/usr/bin/node

const argv = process.argv[2];

if (!argv || isNaN(argv)) {
  console.log('Missing size');
} else {
  for (let i = parseInt(argv); i > 0; i--) {
    console.log('X'.repeat(parseInt(argv)));
  }
}
