class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands = 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1':
                return
            grid[i][j] = '0' # Mark as visited
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    islands += 1
        
        return islands