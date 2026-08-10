# This is the solution for the this problem on hackerrrank.
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#
#
# i. 
# 0. r[0] = a[4] - 5
# 1 i+d = 5 -> 5-5=0
# 2
# 3
#   i.       
# 1 2 3 4 5

#

def rotLeft(a, d):
    # Write your code here
    r = [None] * len(a)
    for i in range(0, len(a)):
        j = i+d if i+d < len(a) else abs(len(a)-i-d)
        r[i] = a[j]
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

