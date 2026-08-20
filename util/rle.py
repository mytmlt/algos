def rle(s: str) -> list[tuple[str, int]]:
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
    import sys

    s = sys.argv[1] if len(sys.argv) > 1 else input().strip()
    print(rle(s))
