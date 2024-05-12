class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """

        window_size = 3

        def get_max(p, g):
            max_val = 0
            for i in range(window_size):
                for j in range(window_size):
                    max_val = max(max_val, g[p[0] + i][p[1] + j])
            return max_val

        res = []
        for i in range(len(grid) - window_size + 1):
            res.append([None] * (len(grid) - window_size + 1))
            for j in range(len(res[i])):
                res[i][j] = get_max((i, j), grid)

        return res