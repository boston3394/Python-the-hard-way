ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait, there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: ##len is number of items in a list
    next_one = more_stuff.pop()
#list.pop([i])Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)
    print "Adding: ", next_one
    stuff.append(next_one) #takes it from the bottom of the list
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] #whoa! fancy
print stuff.pop()
print ' '.join(stuff) #what? cool. joins items with '' between them. aha!
print '#'.join(stuff[3:5]) #very cool joins item 3 and four on the list. does NOT have item 5.

#Objects are an encapsulation of variables and functions into a single entity. Objects get their variables and functions from classes. Classes are essentially a template to create your objects.What is a class? Think of a class as a blueprint. It isn't something in itself, it simply describes how to make something. You can create lots of objects from that blueprint - known technically as an instance.

#A: dir(something) gives you all the attributes of the object. The class is like the blueprint for the house.
