people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5
#a += b is essentially the same as a = a + b, except that:

#+ always returns a newly allocated object, but += should (but doesn't have to) modify the object in-place if it's mutable (e.g. list or dict, but int and str are immutable).
#In a = a + b, a is evaluated twice.

#dogs += 5 is dogs = dogs + 5 so it makes it equal to people 
if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs. "

if people == dogs:
    print "peple are dogs."
