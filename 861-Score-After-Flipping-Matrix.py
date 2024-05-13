class Solution(object):
    def matrixScore(self, grid):
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]
        
        for j in range(1, n):
            count_ones = sum(grid[i][j] for i in range(m))
            if count_ones < m - count_ones:
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]
        
        score = 0
        for row in grid:
            num = int(''.join(map(str, row)), 2)
            score += num
        
        return score