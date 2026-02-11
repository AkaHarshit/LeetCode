class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        c = 0
        for i in range(n - 1):
            l = i + 1
            r = n - 1
            pos = n   

            while l <= r:
                m = (l + r) // 2
                if nums[m] >= target - nums[i]:
                    pos = m
                    r = m - 1
                else:
                    l = m + 1
            c += max(0, pos - (i + 1))
        return c