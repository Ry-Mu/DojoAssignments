import threading

class BuckysMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = BuckysMessenger(name='Send out messages')
y = BuckysMessenger(name="recieve Messages")
x.start()
y.start()

# def function_that_prints():
#     print "I printed"
#
# def function_that_returns():
#     return "I returned"
#
# f1 = function_that_prints()
# f2 = function_that_returns()
# print "Now let us see what the values of f1 and f2 are"
# print f1
# print f2
