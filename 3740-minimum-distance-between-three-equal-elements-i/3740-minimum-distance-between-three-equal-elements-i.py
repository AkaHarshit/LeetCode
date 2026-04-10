class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        index_map = {}
        for i in range(len(nums)):
            if nums[i] not in index_map:
                index_map[nums[i]] = []
            index_map[nums[i]].append(i)
        
        ans = float('inf')
        for indices in index_map.values():
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    dist = 2 * (indices[i+2] - indices[i])
                    if dist < ans:
                        ans = dist
        
        return ans if ans != float('inf') else -1