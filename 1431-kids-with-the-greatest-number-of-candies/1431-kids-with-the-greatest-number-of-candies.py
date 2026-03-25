class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        c = max(candies)   
        lst = []
        for i in candies:          
            if i + extraCandies >= c:
                lst.append(True)
            else:
                lst.append(False)
        
        return lst