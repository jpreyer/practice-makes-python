import re

fn = open ("/etc/passwd", 'r')
d = {}
filelines = fn.readlines()
for i in filelines:
    pattern = re.compile("^#")
    if  pattern.match(i):
        pass
    else:
        un = i.split(':');
        d[un[0]] = un[2]

for j in d.keys():
    print j,d[j]
