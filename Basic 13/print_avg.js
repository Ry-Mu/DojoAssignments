function printAverage(arr){
  var sum = 0
  for (var i = 0; i < arr.length; i++) {
    sum += arr[i];
  }
  var avg = sum/arr.length;
  console.log(avg);
}

printAverage([1,3,4,6,8,9]);