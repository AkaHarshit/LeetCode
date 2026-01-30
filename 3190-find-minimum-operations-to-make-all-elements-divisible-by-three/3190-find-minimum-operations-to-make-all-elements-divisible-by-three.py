class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = 0
        
        for x in nums:
            r = x % 3
            if r != 0:
                c += 1
        
        return c