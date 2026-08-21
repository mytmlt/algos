import os


def triplets(a, b, c):
    ans = 0

    # Deduplicate all arrays; sort A and C for binary search
    a = sorted(set(a))
    b = set(b)
    c = sorted(set(c))

    for q in b:
        p = count_less_or_equal(a, q)
        r = count_less_or_equal(c, q)
        ans += p * r

    return ans


def count_less_or_equal(arr, val):
    l, r = 0, len(arr) - 1
    c = 0

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] <= val:
            c = mid + 1
            l = mid + 1
        else:
            r = mid - 1

    return c


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])
    lenb = int(lenaLenbLenc[1])
    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))
    arrb = list(map(int, input().rstrip().split()))
    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + "\n")

    fptr.close()
