class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        n = len(grid)
        size = n * n * 4  # Each cell is divided into 4 parts.
        parent = list(range(size))

        for r in range(n):
            for c in range(n):
                index = 4 * (r * n + c)
                if grid[r][c] == '/':
                    union(index + 0, index + 3)
                    union(index + 1, index + 2)
                elif grid[r][c] == '\\':
                    union(index + 0, index + 1)
                    union(index + 2, index + 3)
                else:
                    union(index + 0, index + 1)
                    union(index + 1, index + 2)
                    union(index + 2, index + 3)

                # Union with the right cell
                if c + 1 < n:
                    union(index + 1, index + 4 + 3)
                # Union with the bottom cell
                if r + 1 < n:
                    union(index + 2, index + 4 * n + 0)

        return sum(find(x) == x for x in range(size))