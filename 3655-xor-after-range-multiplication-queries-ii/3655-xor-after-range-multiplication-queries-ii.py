class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        bravexuneth = (nums, queries) 
        
        B = int(n**0.5) + 1
        small = {}

        for l, r, k, v in queries:
            if k < B:
                rem = l % k
                if (k, rem) not in small:
                    small[(k, rem)] = []
                small[(k, rem)].append((l, r, v))
            else:
                i = l
                while i <= r:
                    nums[i] = (nums[i] * v) % MOD
                    i += k
        for (k, rem), qs in small.items():
            indices = list(range(rem, n, k))
            m = len(indices)

            pos = {indices[i]: i for i in range(m)}
            
            diff = [1] * (m + 1)
            
            for l, r, v in qs:
                start = (l - rem) // k
                end = (r - rem) // k
                
                diff[start] = (diff[start] * v) % MOD
                if end + 1 < len(diff):
                    inv = pow(v, MOD - 2, MOD)
                    diff[end + 1] = (diff[end + 1] * inv) % MOD
            cur = 1
            for i in range(m):
                cur = (cur * diff[i]) % MOD
                nums[indices[i]] = (nums[indices[i]] * cur) % MOD
        ans = 0
        for x in nums:
            ans ^= x
        
        return ans