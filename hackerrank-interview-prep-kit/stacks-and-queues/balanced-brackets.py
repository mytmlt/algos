import os


def isBalanced(s):
    opening = {"{": 0, "[": 1, "(": 2}
    closing = {"}": 0, "]": 1, ")": 2}

    stack = []

    for c in s:
        if c in closing:
            if (
                len(stack) > 0
                and stack[-1] in opening
                and opening[stack[-1]] == closing[c]
            ):
                stack.pop(-1)
            else:
                return "NO"
        else:
            stack.append(c)

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + "\n")

    fptr.close()
