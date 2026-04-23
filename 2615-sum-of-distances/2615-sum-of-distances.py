class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[nums[i]] = []
            mp[nums[i]].append(i)
        res = [0] * len(nums)
        for val in mp:
            pos = mp[val]
            n = len(pos)
            prefix = [0] * n
            prefix[0] = pos[0]
            for i in range(1, n):
                prefix[i] = prefix[i-1] + pos[i]
            for i in range(n):
                if i > 0:
                    left = pos[i] * i - prefix[i-1]
                else:
                    left = 0
                if i < n - 1:
                    right = (prefix[n-1] - prefix[i]) - pos[i] * (n - i - 1)
                else:
                    right = 0
                res[pos[i]] = left + right
        return res