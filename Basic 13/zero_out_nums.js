function zero_out_nums(arr) {
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] < 0) {
      arr[i] = 0;
  }
}
  return (arr);
}

console.log(zero_out_nums(([1,-3,-4,-6,8,9])));
