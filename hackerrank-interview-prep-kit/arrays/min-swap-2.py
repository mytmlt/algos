import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    visited = [False]*len(arr)
    
    for i in range(len(visited)):
        if visited[i]:
            continue
        s = 0 
        j = i    
        while True:
            visited[j] = True
            
            if arr[j] != j + 1:
                s += 1
                j = arr[j] - 1 
            
            if i == j:
                break     
        
        if s > 0:
            swaps += (s - 1)
    
    print(visited)
    return swaps       
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

