# Check which numbers each card got right, getting that much as copies of next cards

import sys
from itertools import zip_longest

total = 0
with open(sys.argv[1], 'r') as f:
    next_copy_values = []
    for line in f:
        line = line.split(':')[1].split('|')
        winning_set = set(line[0].split())
        drawn_set = set(line[1].split())

        card_instances = 1
        if len(next_copy_values)>0:
            card_instances += next_copy_values[0]
            next_copy_values = next_copy_values[1:]
        total += card_instances

        matching_set = winning_set & drawn_set
        current_copy_values = len(matching_set)*[card_instances]
        # next_copy_values[i] += current_copy_values[i], but for variable lenghts
        next_copy_values = [sum(x) for x in zip_longest(next_copy_values, current_copy_values, fillvalue=0)]

print(total)
