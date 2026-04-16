class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        l = [False] * n  
        c = 0
        for i in range(n):
            p = False
            for j in range(n):
                if not l[j] and baskets[j] >= fruits[i]:
                    l[j] = True
                    p = True
                    break  
            if not p:
                c += 1
        return c