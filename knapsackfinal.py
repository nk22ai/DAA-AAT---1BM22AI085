import sys
import os
import math
import random

def unboundedKnapsack(k, arr):
    b = [False] * (k + 1)
    b[0] = True
    for n in arr:
        for j in range(n, k + 1):
            if b[j - n]:
                b[j] = True
    max_s = 0
    for j in range(k, 0, -1):
        if b[j]:
            max_s = j
            break
    return max_s

if __name__ == '__main__':
    input_data = sys.stdin.read().strip().split('\n')
    
    t = int(input_data[0])
    
    index = 1
    results = []
    
    for _ in range(t):
        n, k = map(int, input_data[index].split())
        arr = list(map(int, input_data[index + 1].split()))
        result = unboundedKnapsack(k, arr)
        results.append(result)
        index += 2
    
    for result in results:
        print(result)
