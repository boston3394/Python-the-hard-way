from sys import argv

script, user_name = argv
#Line 3 "unpacks" argv so that, rather than holding all the arguments, it gets assigned to four variables you can work with: script, first, second, and third. This may look strange, but "unpack" is probably the best word to describe what it does. It just says, "Take whatever is in argv, unpack it, and assign it to all of these variables on the left in order."
prompt = '> '
#We make a variable prompt that is set to the prompt we want, and we give that to raw_input instead of typing it over and over. Now if we want to make the prompt something else, we just change it in this one spot and rerun the script. Very handy.
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

#remember when you run this you have to give the script your name for the argv values

# Make sure you understand how I combined a """ style multiline string with
# the % format activator as the last print.
#------------------------------------------------------------------------------
# Triple quotes strings multiple lines of test together and prints them as one.
# Below is an example:
#print"""
#So I have this paragraph
#and in this paragraph I don't want to use
#print at the beginning of each line
#so instead of using print at the beginning of each line
#I just use triple quotes"""
