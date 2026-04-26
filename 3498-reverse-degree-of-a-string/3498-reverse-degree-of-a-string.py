class Solution:
    def reverseDegree(self, s: str) -> int:
        c = 0
        for i in range(len(s)):
            v = 26 - (ord(s[i]) - ord('a'))
            c += v * (i + 1)
        return c