class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        c = 0
        for i in nums:
            c |= i
        self.count = 0
        n = len(nums)
        def dfs(idx, cur):
            if idx == n:
                if cur == c:
                    self.count += 1
                return
            dfs(idx + 1, cur | nums[idx])
            dfs(idx + 1, cur)
        dfs(0, 0)
        return self.count