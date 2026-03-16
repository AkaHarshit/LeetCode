class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        
        sums = set()
        
        for i in range(m):
            for j in range(n):
                sums.add(grid[i][j])
                
                k = 1
                while True:
                    if i-k < 0 or i+k >= m or j-k < 0 or j+k >= n:
                        break
                    total = 0
                    for d in range(k):
                        total += grid[i-k+d][j+d]     
                        total += grid[i+d][j+k-d]    
                        total += grid[i+k-d][j-d]    
                        total += grid[i-d][j-k+d]      
                    
                    sums.add(total)
                    k += 1
        return sorted(sums, reverse=True)[:3]