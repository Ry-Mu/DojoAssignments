//set myNUmber to 42. Set myName to your name.
//Now swap myNumber into myName & vice versa.

var myNumber = 42;
var myName = "Ryan";

var temp = myNumber;
myNumber = myName;
myName = temp;

console.log(myName);
console.log(myNumber);
