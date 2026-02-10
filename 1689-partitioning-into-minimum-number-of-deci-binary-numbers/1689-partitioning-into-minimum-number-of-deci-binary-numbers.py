class Solution:
    def minPartitions(self, n: str) -> int:
        c = 0
        for i in n:
            if int(i) > c:
                c = int(i)
        return c