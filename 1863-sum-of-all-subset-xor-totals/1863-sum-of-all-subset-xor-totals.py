class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        c = 0
        
        for i in nums:
            c |= i
        
        return c * (1 << (len(nums) - 1))