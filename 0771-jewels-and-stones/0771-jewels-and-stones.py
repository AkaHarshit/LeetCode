class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = {}
        for j in jewels:
            d[j] = True
        c = 0
        for s in stones:
            if s in d:
                c += 1
        return c