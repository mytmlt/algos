from collections import defaultdict

# optimal - don't understand it fully
def sherlockAndAnagrams(s):
    freq_map = defaultdict(int)
    n = len(s)
    ans = 0

    for i in range(n):
        char_counts = [0] * 26
        for j in range(i, n):
            char_counts[ord(s[j]) - ord('a')] += 1
            key = tuple(char_counts)
            
            # Every time we encounter an existing anagram signature,
            # it forms a new pair with every previous occurrence of that signature.
            ans += freq_map[key]
            freq_map[key] += 1

    return ans


# old solution 
# #!/bin/python3

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    l = len(s)
    d = dict()
    r = 0
    
    for sub_len in range(1, l):
        for i, _ in enumerate(s):
            if i + sub_len > l:
                continue
            else:
                ss = ''.join(sorted(s[i:i+sub_len]))
                if ss in d:
                    d[ss] += 1
                else:
                    d[ss] = 1

    for k,v in d.items():
        if v >= 2:
            c = math.comb(v, 2)
            r += c

    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

