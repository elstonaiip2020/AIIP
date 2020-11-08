"""mapper.py"""

import sys

# input for this step comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # split the line and select the two columns needed
    items = line.split(',')
    print('%s\t%s' % (items[3].lower(), items[7]))
