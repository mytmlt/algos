#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    aa = [0] * 26
    bb = [0] * 26
    
    for c in list(a):
        aa[ord(c) - ord('a')] =+ 1
    
    for c in list(b):
        bb[ord(c) - ord('a')] =+ 1
        
    r = 0
    
    for i in range(len(aa)):
        fptr.write(f'char {chr(ord("a") + i)} is {abs(aa[i] - bb[i])}\n')
        r += abs(aa[i] - bb[i])
    
    return r
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

