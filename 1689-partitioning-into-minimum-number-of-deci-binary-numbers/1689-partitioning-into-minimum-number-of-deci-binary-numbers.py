class Solution:
    def minPartitions(self, n: str) -> int:
        c = 0
        for i in n:
            d = ord(i) - ord('0') 
            if d > c:
                c = d
        return c