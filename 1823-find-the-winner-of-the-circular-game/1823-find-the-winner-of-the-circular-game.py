class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        c = 0  
        
        for i in range(1, n + 1):
            c = (c + k) % i
        
        return c + 1