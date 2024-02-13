#!/usr/bin/node
const fs = require('fs');
const inf1 = fs.readFileSync(process.argv[2], 'utf8');
const inf2 = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], inf1 + inf2);
