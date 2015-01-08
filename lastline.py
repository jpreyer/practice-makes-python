print "enter filename; "
filename = raw_input()

fn = open (filename, 'r')

filelines = fn.readlines()

#numlines =len(filelines)
print filelines[-1],
