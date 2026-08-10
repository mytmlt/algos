import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    r = 0
    for i in range(len(q)):
        d = q[i] - (i+1)
        if d > 2:
            print("Too chaotic")
            return 
        b = 0
        # I don't understand this range logic here. It's a necessary opmtimization.
        for j in range(max(0, q[i]-2), i):
            if q[i] < q[j]:
                b += 1            
        r += b    
    print(r)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

