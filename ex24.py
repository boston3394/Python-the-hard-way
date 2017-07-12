print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
#\t is for tab. th 3 quotes is because of escape characters
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprhend passion from intuition
and requires and explanation
\n\t\twhere there is none.
"""

print "-----------------"
print poem
print "-----------------"

five = 10 -2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point) #This is how it gets the values. beans instead of jelly beans is just to hold the value.

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates" % (beans, jars, crates)

start_point = start_point /10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)#you give the function the start point defined earlier in the script

#Why do you you call the variable jelly_beans but the name beans later?
#That's part of how a function works. Remember that inside the function the variable is temporary. When you return it then it can be assigned to a variable for later. I'm just making a new variable named beans to hold the return value.
#What do you mean by reading the code backward?
#Start at the last line. Compare that line in your file to the same line in mine. Once it's exactly the same, move up to the next line. Do this until you get to the first line of the file.
#Who wrote that poem?
#I did. Not all of my poems suck.
