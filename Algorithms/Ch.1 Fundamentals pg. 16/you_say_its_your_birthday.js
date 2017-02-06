//If 2 given numbers represent your birth month and day in either order, log
//How did you know?, else log 'just another day.....'

var day = 6;
var month = 3;

function bDay (x, y) {
	if (x == day && y == month || y == day && x == month) {
		console.log('How did you know?')
	}
	else {
		console.log('Just another day.')
	}
}

bDay(7,5);
