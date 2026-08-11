#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#
def activityNotifications(expenditure, d):
    counts = [0]*201

    for i in range(d):
        counts[expenditure[i]] += 1

    n = 0
    for i in range(d, len(expenditure)):
        m = get_median(counts, d)
        if expenditure[i] >= m * 2:
            n += 1

        counts[expenditure[i]] += 1
        counts[expenditure[i-d]] -= 1
        
    return n
    
def get_median(counts, d): 
    if d % 2 == 0:
        t1, t2 = d // 2, d // 2 + 1
        s = 0
        m1 = None
        for i, c in enumerate(counts):
            s += c
            if m1 is None and s >= t1:
                m1  = i 

            if s >= t2:
                return (m1 + i) / 2
                
    else:
        t = d // 2 + 1 
        s = 0
        for i, c in enumerate(counts):
            s += c
            if s >= t:
                return i 
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()

