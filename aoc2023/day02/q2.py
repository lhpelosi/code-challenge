# Computes the power of each game multiplying the necessary amount of each color

import sys
import re

red_re = re.compile(r"(\d+) red")
green_re = re.compile(r"(\d+) green")
blue_re = re.compile(r"(\d+) blue")

total = 0
with open(sys.argv[1], 'r') as f:
    for line in f:

        red_match = red_re.findall(line)
        red_max = max(map(int, red_match))
        green_match = green_re.findall(line)
        green_max = max(map(int, green_match))
        blue_match = blue_re.findall(line)
        blue_max = max(map(int, blue_match))
        total += red_max * green_max * blue_max

print(total)
