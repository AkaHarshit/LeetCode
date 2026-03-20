class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        
        m = len(grid)
        n = len(grid[0])
        
        result = []
        
        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                arr = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        arr.append(grid[x][y])
                arr = list(set(arr))
                if len(arr) <= 1:
                    row.append(0)
                    continue
                arr.sort()
                min_diff = float('inf')
                
                for t in range(1, len(arr)):
                    diff = arr[t] - arr[t - 1]
                    if diff < min_diff:
                        min_diff = diff
                
                row.append(min_diff)
            
            result.append(row)
        
        return result