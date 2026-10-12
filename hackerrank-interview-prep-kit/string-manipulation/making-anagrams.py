import os
import sys


def makeAnagram(a, b):
    aa = [0] * 26
    bb = [0] * 26

    for c in a:
        aa[ord(c) - ord('a')] += 1

    for c in b:
        bb[ord(c) - ord('a')] += 1

    r = 0

    for i in range(26):
        r += abs(aa[i] - bb[i])

    return r


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

