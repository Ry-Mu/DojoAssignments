//Write a function that determines whether a given year is a leap year. If a year
//If a year is divisble by four, it is a leap year, unless it is divisble by 100.
//However if it is divisible by 400, then it is.

function leapYear (year) {
	if (year % 400 == 0) {
		console.log('Yes!')
	}
	else if (year % 100 == 0) {
		console.log('No!')
	}
	else if (year % 4 == 0) {
		console.log('Yes!')
	}
	else {
		console.log('No!')
	}
}
leapYear(1992)
