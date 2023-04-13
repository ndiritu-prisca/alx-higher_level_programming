#!/usr/bin/node

const fs = require('fs');

const [, , fileA, fileB, fileC] = process.argv;

const textA = fs.readFileSync(fileA, 'utf8');
const textB = fs.readFileSync(fileB, 'utf8');
const textC = textA + textB;

fs.writeFileSync(fileC, textC);
