#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    char_to_freq = Counter(s)
    freq_to_occ = Counter(char_to_freq.values())
    
    freq = list(freq_to_occ.keys())
    if len(freq) > 2:
        return 'NO'
    elif len(freq) == 1:
        return 'YES'
    else:
        # exactly 2 frequencies
        l, h = min(freq), max(freq)
        if l == 1 and freq_to_occ[l] == 1:
            return 'YES'
        elif h - l == 1 and freq_to_occ[h] == 1:
            return 'YES'
        else:
            return 'NO'
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

