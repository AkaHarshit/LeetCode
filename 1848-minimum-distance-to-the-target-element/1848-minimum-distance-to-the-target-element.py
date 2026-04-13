class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        m = float('inf')
        
        for i in range(len(nums)):
            if nums[i] == target:
                d = abs(i - start)
                if d < m:
                    m = d
        return m