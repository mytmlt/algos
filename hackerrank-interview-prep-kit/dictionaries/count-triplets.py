import math
import os
import random
import re
import sys
from collections import Counter, defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    left_map = defaultdict(int)
    right_map = Counter(arr)
    total = 0

    if len(right_map) == 1 and r == 1:
        k = next(iter(right_map))
        return math.comb(right_map[k], 3)
    
    for x in arr:
        if x % r == 0:
            total += left_map[x/r] * right_map[x*r]
        
        left_map[x] += 1
        right_map[x] -= 1
    
    return total

if __name__ == '__main__':
    arr = [int(x) for x in "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1".split(" ")] 

    r = 1 

    ans = countTriplets(arr, r)

    print(ans)
