# Get numbers adjacent to symbols

import sys
import re

number_re = re.compile(r"(\d+)")
symbol_re = re.compile(r"[^0-9.\s]")

number_pos_list = []
symbol_pos_list = []

line_current = 0
with open(sys.argv[1], 'r') as f:
    for line in f:

        for number in number_re.finditer(line):
            number_pos_list += [(int(number.group()), line_current,
                                 number.start(), number.end()-1)]

        for symbol in symbol_re.finditer(line):
            symbol_pos_list += [(line_current, symbol.start())]

        line_current += 1

total = 0
for (number, n_line, n_column_start, n_column_end) in number_pos_list:
    for (s_line, s_column) in symbol_pos_list:
        is_adjacent = (abs(n_line-s_line)<=1 and
                       s_column >= n_column_start-1 and
                       s_column <= n_column_end+1)
        if is_adjacent:
            total += number
            break
print(total)
