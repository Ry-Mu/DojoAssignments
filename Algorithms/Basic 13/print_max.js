function print_max(arr) {
  var max = arr[0];
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] > max);
      max = arr[i];
  }
  return (max);
}

console.log(print_max(([1,3,4,6,8,9])));
