class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n=len(piles)//3
        c=0
        i=len(piles)-2
        for j in range(n):
            c+=piles[i]
            i-=2
        return c