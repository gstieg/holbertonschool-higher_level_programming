#!/usr/bin/node
if (Number.isNaN(parseInt(process.argv[2]))) {
    console.log('Not a number');
} else {
    console.log(parseInt(process.argv[2]));
}
