# Compute the many ways in a race that the record can be broken.
# Each unit of time charging at the start gives +1 speed boost.
# distance = (limit_time-charge_time)*charge_time
# Changes from q1 only removing whitespaces from input

import sys
import io
import math

race_values = []
with open(sys.argv[1], 'r') as f:
    time_list = f.readline().replace(' ','').split(':')[1].strip()
    distance_list = f.readline().replace(' ','').split(':')[1].strip()
    race_values = [(time_list, distance_list)]

total = 1
for limit_time, record_distance in race_values:

    # Find two roots for min and max charge values
    # D = (T-c)*c
    # D = T*c - c**2
    # c**2 - T*c + D = 0
    b = -1.0*float(limit_time)
    c = float(record_distance)
    r1 = (-b - math.sqrt(b**2-4.0*c))/2.0
    r2 = (-b + math.sqrt(b**2-4.0*c))/2.0

    # Count integers between them
    n = math.ceil(r2)-math.floor(r1)-1
    total *= n

print(total)
