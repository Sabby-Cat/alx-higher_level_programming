#!/usr/bin/node
const argv = process.argv;
const s = parseInt(argv[2]);
const chr = 'X';
if (isNaN(s)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < s; i++) {
    console.log(chr.repeat(s));
  }
}
