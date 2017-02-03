function swapNegVals (arr) {
  for (var i = 0; i < arr.length; i++){
    if ( arr[i] > 0) {
      arr[i] = "Dojo";
    }
}
return arr;
}
console.log(swapNegVals([-5,-7,5,7,10]));
