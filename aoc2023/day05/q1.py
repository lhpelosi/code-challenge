# Map numbers through multiple range functions

import sys
import re

map_function_re = re.compile(r"(\d+) (\d+) (\d+)")

def run_maps(numbers, map_function_list):
    for i, n in enumerate(numbers):
        for map_function_values in map_function_list:
            destination_start, source_start, rangelen = map_function_values
            if n >= source_start and n < source_start+rangelen:
                    numbers[i] += destination_start - source_start
                    break

numbers = []
map_function_list = []
with open(sys.argv[1], 'r') as f:
    for iline, line in enumerate(f):

        if (iline==0):
            numbers = list(map(int, line.split(':')[1].split()))
            continue

        if line.endswith("map:\n"):
            run_maps(numbers, map_function_list)
            map_function_list = []
            continue

        map_function_match = map_function_re.match(line)
        if map_function_match:
            map_function_list.append(tuple(map(int, map_function_match.groups())))

    run_maps(numbers, map_function_list)
    print(min(numbers))
