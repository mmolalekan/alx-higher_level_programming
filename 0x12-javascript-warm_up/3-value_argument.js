#!/usr/bin/node

const argv = process.argv;
let foundArgument = false;

argv.forEach((val, idx) => {
  if (idx === 2) {
    foundArgument = true;
    console.log(`${val}`);
  }
});

if (!foundArgument) {
  console.log('No argument');
}
