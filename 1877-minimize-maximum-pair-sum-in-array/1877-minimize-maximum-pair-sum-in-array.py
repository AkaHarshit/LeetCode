class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        c = 0
        while l < r:
            s = nums[l] + nums[r]
            if s > c:
                c = s
            l += 1
            r -= 1
        return c