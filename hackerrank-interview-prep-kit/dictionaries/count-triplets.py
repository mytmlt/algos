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

    for x in arr:
        right_map[x] -= 1
    
        if x % r == 0:
            total += left_map[x//r] * right_map[x*r]
        
        left_map[x] += 1

    return total

if __name__ == '__main__':
    fptr = sys.stdin

    n, r = map(int, fptr.readline().rstrip().split())
    arr = list(map(int, fptr.readline().rstrip().split()))

    ans = countTriplets(arr, r)

    print(ans)
