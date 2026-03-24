class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        r = s[:k][::-1]
        r_p = s[k:]
        return r + r_p