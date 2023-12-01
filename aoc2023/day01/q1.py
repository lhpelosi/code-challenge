# Join first and last digits of each line and sum the lines.

import sys

total = 0
with open(sys.argv[1], 'r') as f:
    for line in f:
        numbers = list(filter(str.isdigit, line))
        total += int(numbers[0] + numbers[-1])

print(total)
