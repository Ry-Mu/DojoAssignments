# OOP Bike

# define the Bike class
class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

        #have this method display the bike's price, maximum speed, and the total miles.
    def displayInfo(self):
        print 'Bike price is: $' + str(self.price)
        print 'Max speed:' + str(self.max_speed) + 'mph'
        print "Total miles:" + str(self.miles) + "miles"

    #ride() - have it display "riding on the screen and increase the toal miles ridden by 10. "
    def ride(self):
        print "Riding"
        self.miles += 10

    #reverse() - have it displau "reversing" on the screen and decrease the total ridden by 5..
    def reversing(self):
        print "Reversing"
        #to prevent negative numbers
        if self.miles >= 5:
            self.miles -= 5


# have the first instnace ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayinfo(). Have the third instance reverse three times and displayInfo().

#what would you do to prevent the instance from having negative numbers?

#create instances and run methods
bike1 = Bike(200, 60)
bike1.ride()
bike1.reversing()
bike1.displayInfo()

bike2 = Bike(250, 65)
bike2.ride()
bike2.reversing()
bike2.displayInfo()
