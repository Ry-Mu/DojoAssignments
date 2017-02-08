#Part I
#Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use an array to do this exercise.

for count in range(1,1000,2):
    print count

#part 2
#Create another program that prints all the multiples of 5 from 5 to 1,000,000.

for count in range(5,100005,5):
    print count

#sum list
#Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
b = sum(a)
print b

#Average list
#Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
b = sum(a)
c= b/len(a)
print c
