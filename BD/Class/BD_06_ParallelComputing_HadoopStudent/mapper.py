"""mapper.py"""
# fill in code
import sys

# input for this step comes from STDIN (standard input)
for line in sys.stdin:
    
    # remove leading and trailing whitespace
    data = line.strip()
    # split the line and select the columns needed
    name, year,grade,course = data.split(',')
    print ("{0}\t{1} {2}".format(course,grade,name))
