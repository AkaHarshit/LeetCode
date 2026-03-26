class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        from collections import Counter
        
        total = 0
        bottom = Counter()
        
        for row in grid:
            for val in row:
                total += val
                bottom[val] += 1
        
        top = Counter()
        top_sum = 0
        for i in range(m - 1):
            for val in grid[i]:
                top[val] += 1
                bottom[val] -= 1
                if bottom[val] == 0:
                    del bottom[val]
                top_sum += val
            
            bottom_sum = total - top_sum
            
            if top_sum == bottom_sum:
                return True
            
            diff = abs(top_sum - bottom_sum)
            if top_sum > bottom_sum:
                if self.valid_remove(top, grid, 0, i, 0, n-1, diff):
                    return True
            else:
                if self.valid_remove(bottom, grid, i+1, m-1, 0, n-1, diff):
                    return True
        left = Counter()
        right = Counter()
        total = 0
        
        for j in range(n):
            for i in range(m):
                val = grid[i][j]
                right[val] += 1
                total += val
        
        left_sum = 0
        
        for j in range(n - 1):
            for i in range(m):
                val = grid[i][j]
                left[val] += 1
                right[val] -= 1
                if right[val] == 0:
                    del right[val]
                left_sum += val
            
            right_sum = total - left_sum
            
            if left_sum == right_sum:
                return True
            
            diff = abs(left_sum - right_sum)
            
            if left_sum > right_sum:
                if self.valid_remove(left, grid, 0, m-1, 0, j, diff):
                    return True
            else:
                if self.valid_remove(right, grid, 0, m-1, j+1, n-1, diff):
                    return True
        
        return False
    
    
    def valid_remove(self, counter, grid, r1, r2, c1, c2, target):
        if target not in counter:
            return False
        
        rows = r2 - r1 + 1
        cols = c2 - c1 + 1
        if rows > 1 and cols > 1:
            return True
        if rows == 1:
            if grid[r1][c1] == target:
                return True
            if grid[r1][c2] == target:
                return True
            return False
        if cols == 1:
            if grid[r1][c1] == target:
                return True
            if grid[r2][c1] == target:
                return True
            return False
        
        return False