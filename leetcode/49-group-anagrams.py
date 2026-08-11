from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        for s in strs:
            k = [0] * 26
            for c in s:
                k[ord(c) - ord("a")] += 1

            d[tuple(k)].append(s)

        return d.values()
