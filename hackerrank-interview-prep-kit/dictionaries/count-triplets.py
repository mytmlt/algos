from collections import Counter, defaultdict


def countTriplets(arr, r):
    left_map = defaultdict(int)
    right_map = Counter(arr)
    total = 0

    for x in arr:
        right_map[x] -= 1

        if x % r == 0:
            total += left_map[x // r] * right_map[x * r]

        left_map[x] += 1

    return total
