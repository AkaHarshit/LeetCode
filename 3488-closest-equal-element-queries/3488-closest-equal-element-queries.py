class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        pos = {}
        for i in range(n):
            if nums[i] not in pos:
                pos[nums[i]] = []
            pos[nums[i]].append(i)

        def find_index(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        res = []
        
        for q in queries:
            val = nums[q]
            arr = pos[val]
            
            if len(arr) == 1:
                res.append(-1)
                continue
            
            k = find_index(arr, q)
            left_idx = arr[(k - 1) % len(arr)]
            right_idx = arr[(k + 1) % len(arr)]
    
            d1 = abs(q - left_idx)
            d1 = min(d1, n - d1)
            
            d2 = abs(q - right_idx)
            d2 = min(d2, n - d2)
            
            res.append(min(d1, d2))
        
        return res