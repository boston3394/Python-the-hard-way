
#adds features to your script from th epython feature set. instead of giving you all the modules at once you have to sepcify which you want to use.
#importing the sys module
from sys import argv

#argv is the argument variable. it holds the arguments you pass to the script
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "This variable is called:", raw_input("Enter test input ") 

#So far you have been running command line scripts without arguments.
#Need to run this script like python ex13.py first 2nd 3rd
#EXAMPLES
#$ python ex13.py stuff things that
#The script is called: ex13.py
#Your first variable is: stuff
#Your second variable is: things
#Your third variable is: that
#$
#$ python ex13.py apple orange grapefruit
#The script is called: ex13.py
#Your first variable is: apple
#Your second variable is: orange
#Your third variable is: grapefruit
