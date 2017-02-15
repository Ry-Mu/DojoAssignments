#newBoston episode 29 - classes and objects

class Tuna:
    def __init__(self):
        print('Bmkfirfnriji')   # This part of the code is executed everytime an object is created. First thing it does is look for init function and look to do whatever is in function.

    def swim(self):
        print('I am swimming')

flipper = Tuna()
flipper.swim()


#newBoston episode 30 - init

class Enemy:
    def __init__(self, x):
        self.energy = x   #basically whenever we create an enemy, this is what we want it to do.

    def get_energy(self):
        print(self.energy)

jason = Enemy(5)   #Even though we define self earlier when we first created this class, it is not necessary when in puttin that in when we create a new object?
sandy = Enemy(18) #two different enemies from the same class, except different energy levels

jason.get_energy()
sandy.get_energy()

#newBoston episode 31 - classes vs. variabels

class Girl: #side note to always uppcase classes - Girls not girls

    gender = 'female'

    def __init__(self, name):
        self.name = name

r = Girl('Rachel')
s = Girl('Stanky')
print(r.gender)  #instances are unique instances or uses of the given class.Instnaces can vary but classes remain the same. Class is like a template, object is the house or robot shell.
print(s.gender)
print(r.name)
print(s.name)

#newBoston episode 32 - inheritance

#Inheritance is pretty much the same as real life. I inherited my my moms eyes, i inherited my dads nose.
#If your grandpa dies and you inherit the house and the land.
#Pretty much inheritence is getting something from someone else

class Parent():
    def print_last_name(self):
        print('Roberts')


#class Child(): #in the open paranthesis, you can put the name of any class that you want to inherit from.And pass it on to the child
class Child(Parent):

    def print_first_name(self):
        print('Bucky')

bucky = Child()
bucky.print_first_name()
bucky.print_last_name()  #have all the functions from the parents class, inheriting its only function

#also have the ability to override inheritence functions

class Parent():
    def print_last_name(self):
        print('Roberts')

class Child(Parent):

    def print_first_name(self):
        print('Bucky')

    def print_last_name(self):
        print('Snitzleberg')    #In order to overrride, you create a same function, with the same exact name, and put new value.

bucky = Child()
bucky.print_first_name()
bucky.print_last_name()


#newBoston episode 33 - multiple inheritance

#basically a way where we can inherit or get stuff from more than one class



class deck(object):
    def __init__(self, number_of_cards):


        def deal(self):
            pass

        def collect(self):
            pass

        def shuffle(self):
            pass
