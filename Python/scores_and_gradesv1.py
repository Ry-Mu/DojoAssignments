import random
def grades():
    count = 0
    while count <= 10:
        num = random.randint(60,100)
        if num < 70 and num > 60:
            print "Total", num, ": Your grade is a D"
        if num < 80 and num > 70:
            print "Total", num, ": Your grade is a C"
        if num < 90 and num > 80:
            print "Total", num, ": Your grade is a B"
        if num < 100 and num > 90:
            print "Total", num, ": Your grade is a A"
        count+=1
grades()
