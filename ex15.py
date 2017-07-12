from sys import argv

script, filename = argv
#Lines 1-3 uses argv to get a filename. Next we have line 5 where we use a new command open. Right now, run pydoc open and read the instructions. Notice how like your own scripts and raw_input, it takes a parameter and returns a value you can set to your own variable. You just opened a file.

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

txt.close()

#Line 8 prints a little message, but on line 9 we have something very new and exciting. We call a function on txt named read. What you get back from open is a file, and it also has commands you can give it. You give a file a command by using the . (dot or period), the name of the command, and parameters. Just like with open and raw_input. The difference is that txt.read() says, "Hey txt! Do your read command with no parameters!"

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
#code didnt work because I forgot () after read
#error was <built-in method read of file object at >

txt_again.close()
