class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                nums = []
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        nums.append(grid[r][c])
                if sorted(nums) != [1,2,3,4,5,6,7,8,9]:
                    continue
                if (grid[i][j] + grid[i][j+1] + grid[i][j+2] == 15 and
                    grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] == 15 and
                    grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] == 15 and
                    grid[i][j] + grid[i+1][j] + grid[i+2][j] == 15 and
                    grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] == 15 and
                    grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2] == 15 and
                    grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] == 15 and
                    grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] == 15):
                    count += 1
        return count