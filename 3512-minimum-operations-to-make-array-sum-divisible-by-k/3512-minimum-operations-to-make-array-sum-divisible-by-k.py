class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        c=0
        for i in range(len(nums)):
            c+=nums[i]
        return c%k
            
        