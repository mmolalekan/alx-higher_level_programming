#!/usr/bin/node

const argv = process.argv;

if (argv.length === 2) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('argument found');
} else if (argv.length > 3) {
  console.log('Arguments found');
}
