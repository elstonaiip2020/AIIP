"""reducer.py"""

import sys

current_city = None
current_rating = 0
restaurant_count = 0
key = None

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py splitting by '\t'
    city, rating = line.split('\t', 1)
    # convert value (currently a string) to int
    try:
        rating = int(rating)
    except ValueError:
        # ignore/discard this line if value wasn't a number
        continue

    # Since during the shuffling phase outputs from the mappers
    # are sorted before passed to the reduce we can safely
    # stop counting a particular key after the last occurance
    if current_city == city:
        current_rating += rating
        restaurant_count += 1
    else:
        if current_city:
            # write result to STDOUT
            print('%s\t%s' % (current_city, current_rating/restaurant_count))
        current_rating = rating
        restaurant_count = 1
        current_city = city

    # ensure the results for the last key is written to STDOUT
    if current_city == city:
        print('%s\t%s' % (current_city, current_rating/restaurant_count))
