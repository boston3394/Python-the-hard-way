#Commands to remember
#close - closes the file and saves it
#read - reads the contents of a file. can be assigned o a variable.
#readline - reads just one line of a text file
#truncates - empties the file
#write('stuff') - writes to a file

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit return"

#gives a pause to the user if they want to exit out
raw_input("?")

#opens file, assigns it to target and uses 'w' to overwrite
print "Opening the file...."
target = open(filename, 'w')
#If you want to read the file, pass in r
#If you want to read and write the file, pass in r+
#If you want to overwrite the file, pass in w
#If you want to append to the file, pass in a

#deletes the information in file
print "Truncating the file. Goodbye!"
target.truncate()

#gets the raw input from the user and assigns it to variables
print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file"

#takes variables and writes it to the file while writing a line between each
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print "And finally, we close it."
target.close()

#STUDY QUESTIONS
#If you do not understand this, go back through and use the comment trick to get it squared away in your mind. One simple English comment above each line will help you understand or at least let you know what you need to research more.
#Write a script similar to the last exercise that uses read and argv to read the file you just created.
#There's too much repetition in this file. Use strings, formats, and escapes to print out line1, line2, and line3 with just one target.write() command instead of six.
#Find out why we had to pass a 'w' as an extra parameter to open. Hint: open tries to be safe by making you explicitly say you want to write a file.
#If you open the file with 'w' mode, then do you really need the target.truncate()? Read the documentation for Python's open function and see if that's true.
