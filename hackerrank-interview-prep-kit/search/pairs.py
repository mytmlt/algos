import os
from collections import Counter


def pairs(k, arr):
    ans = 0
    c = Counter(arr)

    for a in arr:
        t = a - k
        ans += c[t]

    return ans


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + "\n")

    fptr.close()
