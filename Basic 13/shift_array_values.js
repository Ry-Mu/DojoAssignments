function shift_array(arr){

for(var i = 0; i < arr.length-1; i++){
  arr[i] = arr[i + 1];
}
  arr[arr.length-1] = 0;

console.log(arr);
}

shift_array([1,3,5]);
