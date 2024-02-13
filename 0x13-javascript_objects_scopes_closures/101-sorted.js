#!/usr/bin/node
const dct = require('./101-data').dict;
const newD = {};
for (const key in dct) {
  if (typeof (newD[dct[key]]) === 'undefined') {
    newD[dct[key]] = [];
  }
  newD[dct[key]].push(key);
}
console.log(newD);
