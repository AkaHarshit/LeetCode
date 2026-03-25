class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        total = 0
        for i in range(m):
            for j in range(n):
                total += grid[i][j]
    
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        curr = 0
        for i in range(m - 1):   
            row_sum = 0
            for j in range(n):
                row_sum += grid[i][j]
            
            curr += row_sum
            if curr == target:
                return True
        
        curr = 0
        for j in range(n - 1):   
            col_sum = 0
            for i in range(m):
                col_sum += grid[i][j]
            
            curr += col_sum
            if curr == target:
                return True
        
        return False