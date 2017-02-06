//Based on earlier "Countdown by fours", given lownum, highnum, mult, print multiples of of mult
//from highnum down to lownum using a FOR. For (2,9,3), print 9 6 3 (on successive lines)
function countDown (start, end, count) {
	for (var i = start; i >= end; i -= count) {
		console.log(i)
	}
}
countDown(100, 17, 3)
