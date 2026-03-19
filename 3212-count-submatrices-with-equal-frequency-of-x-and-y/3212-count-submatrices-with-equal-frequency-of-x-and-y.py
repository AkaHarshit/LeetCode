class Solution:
    def numberOfSubmatrices(self, grid):
        n = len(grid)
        m = len(grid[0])
        px = [[0]*(m+1) for _ in range(n+1)]
        py = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(n):
            for j in range(m):
                px[i+1][j+1] = px[i][j+1] + px[i+1][j] - px[i][j]
                py[i+1][j+1] = py[i][j+1] + py[i+1][j] - py[i][j]
                
                if grid[i][j] == 'X':
                    px[i+1][j+1] += 1
                elif grid[i][j] == 'Y':
                    py[i+1][j+1] += 1
        ans = 0
        for i in range(n):
            for j in range(m):
                x = px[i+1][j+1]
                y = py[i+1][j+1]
                
                if x == y and x > 0:
                    ans += 1
        
        return ans