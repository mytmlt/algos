# This is the solution for the this problem on hackerrrank.
# https://www.hackerrank.com/challenges/greedy-florist/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

import os


def getMinimumCost(k, c):
    # The most expensive flowers should get the cheapest multipliers, so
    # sort descending and pair the i-th flower with multiplier i // k + 1.
    c.sort(reverse=True)

    return sum((i // k + 1) * price for i, price in enumerate(c))


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + "\n")

    fptr.close()
