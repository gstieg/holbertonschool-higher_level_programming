#!/usr/bin/node
function factorial (a) {
  if (isNaN(a)) {
      return 1;
  }
  if (a === 0) {
      return 1;
  }
}
console.log(factorial(process.argv[2]));
