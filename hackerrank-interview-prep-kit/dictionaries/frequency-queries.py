#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    r = []
    d1 = defaultdict(int)  # element -> frequency
    d2 = defaultdict(int)  # frequency -> count of elements with this frequency
    
    for c, p in queries:
        if c == 1:
            # snapshot old freq
            old_freq = d1[p]
            if old_freq > 0:
                d2[old_freq] -= 1
            # increase the frequency of p
            d1[p] = old_freq + 1
            
            # increase the freqency of old_frequency + 1
            d2[old_freq + 1] += 1
                
        elif c == 2:
            old_freq = d1[p]
            if old_freq > 0:
                # decrease the frequency of the old freqency
                d2[old_freq] -= 1
                # decrease the frequency of p
                d1[p] = old_freq - 1
                # since one p was removed, we need to increase the freqyency of the one freqyency before it
                d2[old_freq - 1] += 1
            
        elif c == 3:
            r.append(1 if d2[p] > 0 else 0)
    
    return r
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()


