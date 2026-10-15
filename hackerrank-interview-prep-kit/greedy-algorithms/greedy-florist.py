# https://www.hackerrank.com/challenges/greedy-florist/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

import os


def getMinimumCost(k, c):
    c = sorted(c, reverse=True)
    total = 0
    for i in range(len(c)):
        total += (i // k + 1) * c[i]
    return total


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().strip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    c = list(map(int, input().strip().split()))

    result = getMinimumCost(k, c[:n])

    fptr.write(str(result) + "\n")

    fptr.close()
