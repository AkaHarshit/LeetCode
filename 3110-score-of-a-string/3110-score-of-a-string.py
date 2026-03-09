class Solution:
    def scoreOfString(self, s: str) -> int:
        c = 0
        for i in range(len(s) - 1):
            d = ord(s[i]) - ord(s[i+1])
            if d < 0:
                d = -d
            c += d
        return c