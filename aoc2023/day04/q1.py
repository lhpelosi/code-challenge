# Check which numbers each card got right, computing a score

import sys

total = 0
with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.split(':')[1].split('|')
        winning_set = set(line[0].split())
        drawn_set = set(line[1].split())

        matching_set = winning_set & drawn_set
        if len(matching_set) > 0:
            total += 2**(len(matching_set)-1)

print(total)
