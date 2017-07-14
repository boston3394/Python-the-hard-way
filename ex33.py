#while loops
i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i) #appends i to the list. adds the number to list each time it increases

#i += 1 increments numbers.
    i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "
#num doent matter it is just the name of the items inside numbers. You can call them anything, this was confusing to me at first.
for num in numbers:
    print num
