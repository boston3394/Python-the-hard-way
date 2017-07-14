#Loops and lists
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#This first kind of for-loop goes through a List
#what you call the item doesnt matter. was number changed it to banana
for banana in the_count:
    print "This is count %d" % banana

#same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

#we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
#range goes on less than th ehigh number so 0-5
for i in range(0,6):
    print "Adding %d to the list." % i
    #append is a function that lists understand
    elements.append(i)
#added the range to elements
#now we can print them out too
for i in elements:
    print "Element was: %d" % i

#assign range to a list directly.
my_list =list(range(0,6))
print my_list
#V=https://developers.google.com/edu/python/lists good resource on lists 
