# Check which games are possible with a limited amount of each color

import sys
import re

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX =  14

game_id_re = re.compile(r"Game (\d+)")
red_re = re.compile(r"(\d+) red")
green_re = re.compile(r"(\d+) green")
blue_re = re.compile(r"(\d+) blue")

total = 0
with open(sys.argv[1], 'r') as f:
    for line in f:
        is_valid = True
        game_id = int(game_id_re.search(line).groups()[0])

        red_match = red_re.findall(line)
        for n in red_match:
            if int(n) > RED_MAX:
                is_valid = False

        green_match = green_re.findall(line)
        for n in green_match:
            if int(n) > GREEN_MAX:
                is_valid = False

        blue_match = blue_re.findall(line)
        for n in blue_match:
            if int(n) > BLUE_MAX:
                is_valid = False

        if is_valid:
            total += int(game_id)

print(total)
