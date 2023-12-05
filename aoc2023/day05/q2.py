# Map ranges through multiple range functions

import sys
import re

map_function_re = re.compile(r"(\d+) (\d+) (\d+)")

def run_maps(input_range_list, map_function_list):
    output_range_list = []
    while (len(input_range_list)>0):
        range_start, range_end = input_range_list[0]
        input_range_list = input_range_list[1:]

        is_mapped = False
        for map_function_values in map_function_list:
            destination_start, source_start, map_len = map_function_values
            source_end = source_start+map_len-1
            map_delta = destination_start - source_start

            if range_end < source_start or range_start > source_end:
                continue
            is_mapped = True

            # Reinsert unused range parts
            if range_start < source_start:
                input_range_list.append((range_start, source_start-1))
            if range_end > source_end:
                input_range_list.append((source_end+1, range_end))

            output_range_list.append((
                max(range_start, source_start) + map_delta,
                min(range_end, source_end) + map_delta
            ))
            break

        if not is_mapped:
            output_range_list.append((range_start, range_end))

    return output_range_list

ranges = []
map_function_list = []
with open(sys.argv[1], 'r') as f:
    for iline, line in enumerate(f):

        if (iline==0):
            numbers = list(map(int, line.split(':')[1].split()))
            ranges = [(numbers[i], numbers[i]+numbers[i+1]-1) for i in range(0, len(numbers), 2)]
            continue

        if line.endswith("map:\n"):
            ranges = run_maps(ranges, map_function_list)
            map_function_list = []
            continue

        map_function_match = map_function_re.match(line)
        if map_function_match:
            map_function_list.append(tuple(map(int, map_function_match.groups())))

    ranges = run_maps(ranges, map_function_list)
    print(min([start for start, end in ranges]))
