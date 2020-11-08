"""mapper.py"""

import sys

# input for this step comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # split the line into words
    words = line.split()

    for word in words:
        # write each word and count of 1 to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step,
        # tab-delimited; the word count is 1
        print('%s\t%s' % (word, 1))
