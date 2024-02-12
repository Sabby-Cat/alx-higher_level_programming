#!/usr/bin/node
if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  const args = process.argv.slice(2);
  const intAg = args.sort((a, b) => a - b);
  console.log(intAg[intAg.length - 2]);
}
