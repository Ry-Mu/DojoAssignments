//Add odd integers from -300,000 to 300,000, and console.log
//the final sum. Is there a shortcut.

var sum = 0
for (var i = -301; i < 300; i +=2) {
    // console.log(i);
    sum = sum + i;
}
console.log(sum)
