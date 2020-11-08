"""reducer.py"""

import sys

current_key = None
current_value = 0
key = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py splitting by '\t'
    key, value = line.split('\t', 1)

    # convert value (currently a string) to int
    try:
        value = int(value)
    except ValueError:
        # ignore/discard this line if value wasn't a number
        continue

    # Since during the shuffling phase outputs from the mappers
    # are sorted before passed to the reduce we can safely
    # stop counting a particular key after the last occurance
    if current_key == key:
        current_value += value
    else:
        if current_key:
            # write result to STDOUT
            print('%s\t%s' % (current_key, current_value))
        current_value = value
        current_key = key

# ensure the results for the last key is written to STDOUT
if current_key == key:
    print('%s\t%s' % (current_key, current_value))
