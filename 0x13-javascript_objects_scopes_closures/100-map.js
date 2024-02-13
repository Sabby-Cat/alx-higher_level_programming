#!/usr/bin/node
const lst = require('./100-data.js').list;
console.log(lst);
console.log(lst.map((item, index) => item * index));
