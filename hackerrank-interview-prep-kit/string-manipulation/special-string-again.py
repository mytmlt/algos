import os


def substrCount(s):

    count = 0
    rle = build_rle(s)

    # count substrings with same character
    for r in rle:
        count += (r[1] * (r[1] + 1)) // 2

    for i in range(1, len(rle) - 1):
        rl, rm, rr = rle[i - 1], rle[i], rle[i + 1]

        if rm[1] == 1 and rl[0] == rr[0]:
            count += min(rl[1], rr[1])

    return count


def build_rle(s: str) -> list[tuple[str, int]]:
    if not s:
        return []

    count = 1
    result = []
    current_char = s[0]

    for c in s[1:]:
        if current_char == c:
            count += 1
        else:
            result.append((current_char, count))
            count = 1
            current_char = c

    result.append((current_char, count))
    return result


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input())

    s = input()

    result = substrCount(s)

    fptr.write(str(result) + "\n")

    fptr.close()
