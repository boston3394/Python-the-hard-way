#Functions do three things:

#They name pieces of code the way variables name strings and numbers.
#They take arguments the way your scripts take argv.
#Using 1 and 2 they let you make your own "mini-scripts" or "tiny commands."

#THis one i slike your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#ok, that *args is actually pointless, we can just do THis
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#This just takes one argument. dont need () for one arg
def print_one(arg1):
    print "arg1: %r" % arg1

#Don't forget colons
#This next one takes no arguments
def print_none():
    print "I got nothin'."

print_two("zed","shaw")
print_two_again("zed", "shaw")
print_one("First!")
print_none() #remember not to forget parentheses

#First we tell Python we want to make a function using def for "define".
#On the same line as def we give the function a name. In this case we just called it "print_two" but it could also be "peanuts". It doesn't matter, except that your function should have a short name that says what it does.
#Then we tell it we want *args (asterisk args) which is a lot like your argv parameter but for functions. This has to go inside () parentheses to work.
#Then we end this line with a : colon, and start indenting.
#After the colon all the lines that are indented four spaces will become attached to this name, print_two. Our first indented line is one that unpacks the arguments the same as with your scripts.
#FUNCTION = MINI SCRIPT#"To 'run,' 'call,' or 'use' a function all mean the same thing."
#What does the * in *args do?
#That tells Python to take all the arguments to the function and then put them in args as a list. It's like argv that you've been using, but for functions. It's not normally used too often unless specifically needed.
