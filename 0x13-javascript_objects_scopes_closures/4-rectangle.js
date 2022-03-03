#!/usr/bin/node
/**
 * Write a class Rectangle that defines a rectangle:
 * You must use the class notation for defining your class
 */

module.exports = class Rectangle {

    constructor(w, h) {
	if (w > 0 && h > 0) {
	    this.width = w;
	    this.height = h;
	}
    }
    
    print(){
	for (let i = 0; i < this.height; i ++){
	    console.log('X'.repeat(this.width));
	}
    }
    rotate() {
	let Nwidth = this.width;
	let Nheight = this.width;
	this.width = Nwidth;
	this.height = Nheight;
    }

    double() {
	this.width = this.width * 2;
	this.height = this.height *2;
    }
};
