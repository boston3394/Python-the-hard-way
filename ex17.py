from sys import argv
from os.path import exists
#Return True if path refers to an existing path. Returns False for broken symbolic links. On some platforms, this function may return False if permission is not granted to execute os.stat() on the requested file, even if the path physically exists.
script, from_file, to_file = argv
#line 4 specifies which arguments the cmd line will take as you specify the folder to and from
print "Copying from %s to %s" % (from_file, to_file)

#we could do these two on one line, how?
in_file = open(from_file)
#line 9 opens the from file
indata = in_file.read()
#line 11 taks the data from file and assigns it to indata

print "The input file is %d bytes long" % len(indata)
#counts indata

print "Does the output file exist? %r" % exists(to_file)
#checks if it exists (it doesn't)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input

out_file = open(to_file, 'w')
out_file.write(indata)
#creates a new file andopens it and write it.

print "Alright, all done."

out_file.close()
in_file.close()
#closes both files
