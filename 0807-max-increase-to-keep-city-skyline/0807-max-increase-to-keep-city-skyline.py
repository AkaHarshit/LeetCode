class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowMax = [0] * n
        for r in range(n):
            for c in range(n):
                if grid[r][c] > rowMax[r]:
                    rowMax[r] = grid[r][c]
        colMax = [0] * n
        for c in range(n):
            for r in range(n):
                if grid[r][c] > colMax[c]:
                    colMax[c] = grid[r][c]
        totalIncrease = 0
        for r in range(n):
            for c in range(n):
                allowedHeight = min(rowMax[r], colMax[c])
                totalIncrease += allowedHeight - grid[r][c]
        return totalIncrease