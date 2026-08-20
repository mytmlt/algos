from collections import defaultdict


def sherlockAndAnagrams(s):
    freq_map = defaultdict(int)
    n = len(s)
    ans = 0

    for i in range(n):
        char_counts = [0] * 26
        for j in range(i, n):
            char_counts[ord(s[j]) - ord("a")] += 1
            key = tuple(char_counts)

            # Every time we encounter an existing anagram signature,
            # it forms a new pair with every previous occurrence of that signature.
            ans += freq_map[key]
            freq_map[key] += 1

    return ans
