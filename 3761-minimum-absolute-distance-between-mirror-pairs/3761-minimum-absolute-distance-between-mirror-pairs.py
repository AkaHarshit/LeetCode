class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        seen = {}
        ans = float('inf')
        
        for i in range(len(nums)):
            rev = int(str(nums[i])[::-1])
            
            if nums[i] in seen:
                ans = min(ans, i - seen[nums[i]])
            
            seen[rev] = i  
        
        return ans if ans != float('inf') else -1