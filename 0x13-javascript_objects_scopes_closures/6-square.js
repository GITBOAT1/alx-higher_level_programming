#!/usr/bin/node
/**
 * Write a class sQUARE that defines a sQUARE:
 * IT  Must use the class notation for defining your class and extends
 */
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {

    constructor(size) {
	super(size, size)
    }
    charPrint(c) {
	if(!c) {
	    c = 'X';
	}
	for (let i = 0; i < this.height; i++)
	{
	    console.log(c.repeat(this.width));
	}
    }
};
