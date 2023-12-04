# Multiply numbers adjacent to gears ("*")

import sys
import re
from functools import reduce

number_re = re.compile(r"(\d+)")
gear_re = re.compile(r"\*")

number_pos_list = []
gear_pos_list = []

line_current = 0
with open(sys.argv[1], 'r') as f:
    for line in f:

        for number in number_re.finditer(line):
            number_pos_list += [(int(number.group()), line_current,
                                 number.start(), number.end()-1)]

        for gear in gear_re.finditer(line):
            gear_pos_list += [(line_current, gear.start())]

        line_current += 1

total = 0
for (g_line, g_column) in gear_pos_list:
    adjacent_number_list = []
    for (number, n_line, n_column_start, n_column_end) in number_pos_list:
        is_adjacent = (abs(n_line-g_line)<=1 and
                       g_column >= n_column_start-1 and
                       g_column <= n_column_end+1)
        if is_adjacent:
            adjacent_number_list += [number]
    if len(adjacent_number_list)>1:
        total += reduce(lambda x,y: x*y, adjacent_number_list)
print(total)
