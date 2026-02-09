class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        c = 0

        for i in accounts:
            s = sum(i)
            if s > c:
                c = s

        return c