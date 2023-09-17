#!/usr/bin/node
// if (process.argv.length <= 3) {
//   console.log('0');
// } else {
//   const arr = process.argv.slice(2).map(Number);
//   console.log(arr.sort((a, b) => a - b)[arr.length - 2]);
// }
const arr = process.argv;
if (arr.length <= 3) {
  console.log('0');
} else {
  const arrNo = [];
  for (let i = 2; i < arr.length; i++) {
    arrNo.push(parseInt(arr[i]));
  }
  const max = Math.max(...arrNo);
  const newArray = arrNo.filter(item => item !== max);
  console.log(Math.max(...newArray));
}
