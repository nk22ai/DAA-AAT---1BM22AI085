#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPeople' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY p
#  2. LONG_INTEGER_ARRAY x
#  3. LONG_INTEGER_ARRAY y
#  4. LONG_INTEGER_ARRAY r
#

def maximumPeople(p, x, y, r):
    n = len(p)
    m = len(y)
    towns = sorted(zip(x, p))
    clouds = sorted(zip(y, r))
    from collections import defaultdict
    events = []
    for i in range(m):
        start = y[i] - r[i]
        end = y[i] + r[i]
        events.append((start, 'start', i))
        events.append((end + 1, 'end', i))
    for i in range(n):
        events.append((x[i], 'town', p[i]))
    events.sort()
    current_clouds = set()
    sunny_population = 0
    cloud_population = defaultdict(int)
    single_cloud_population = defaultdict(int)
    
    for pos, type_, value in events:
        if type_ == 'start':
            current_clouds.add(value)
        elif type_ == 'end':
            current_clouds.remove(value)
        elif type_ == 'town':
            if len(current_clouds) == 0:
                sunny_population += value
            elif len(current_clouds) == 1:
                cloud_id = next(iter(current_clouds))
                cloud_population[cloud_id] += value
    
    max_population = sunny_population
    for cloud_id in cloud_population:
        max_population = max(max_population, sunny_population + cloud_population[cloud_id])
    return max_population

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()
