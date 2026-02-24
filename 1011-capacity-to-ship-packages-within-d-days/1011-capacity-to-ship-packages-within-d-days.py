class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            d=1
            c=0
            for i in weights:
                if c+i > capacity:
                    d+=1
                    c=0
                c+=i
            return d<=days
        l=max(weights)
        r=sum(weights)
        while l<r:
            m=(l+r)//2
            if canShip(m):
                r=m
            else:
                l=m+1       
        return l