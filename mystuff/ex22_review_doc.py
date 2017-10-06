#Go to https://atom.io/ with your browser, get the Atom text editor, and install it. Use powershell as well
#mkdir mystuff cd mystuff
#print - outputs what you specify
#number sign is a comment
#set variables
#(), >,< +,-, /, *
#%s, %r %r calls repr, while %s calls str. These may behave differently for some types, but not for others: repr returns "a printable representation of an object", while str returns "a nicely printable representation of an object". For example, they are different for strings:

#>>> s = "spam"
#>>> print(repr(s))
#'spam'
#>>> print(str(s))
#spam
#In this case, the repr is the literal representation of a string (which the Python #interpreter can parse into a str object), while the str is just the contents of the string.
#"He's %d inches tall" % my_height
#You should use %s and only use %r for getting debugging information about something. The %r will give you the "raw programmer's" version of variable, also known as the "representation."
#https://learnpythonthehardway.org/book/ex10.html - escape chracters
#raw_input() takes input from the user
#prompt the user - age = "raw_input(How old are you? ")
#The argv is the "argument variable," a very standard name in programming, that you will find used in many other languages. This variable holds the arguments you pass to your Python script when you run it. In the exercises you will get to play with this more and see what happens.

#Line 3 "unpacks" argv so that, rather than holding all the arguments, it gets assigned to four variables you can work with: script, first, second, and third. This may look strange, but "unpack" is probably the best word to describe what it does. It just says, "Take whatever is in argv, unpack it, and assign it to all of these variables on the left in order."

from sys import argv
txt.read

close -- Closes the file. Like File->Save.. in your editor.
read -- Reads the contents of the file. You can assign the result to a variable.
readline -- Reads just one line of a text file.
truncate -- Empties the file. Watch out if you care about the file.
write('stuff') -- Writes "stuff" to the file.
