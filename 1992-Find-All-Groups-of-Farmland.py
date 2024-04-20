class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        lands_p = [] 


        rows, cols = len(land), len(land[0])
        def dfs(i, j, l):
            if i < 0 or i >= rows or j < 0 or j >= cols or land[i][j] != 1:
                return
            land[i][j] = 0
            if len(l) > 2 and (l[2] < i or l[3] < j):
                l[2], l[3] = i, j
            if len(l) == 2:
                l.append(i)
                l.append(j)
            dfs(i + 1, j, l)
            dfs(i, j + 1, l)

        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1:
                    l = [i,j]
                    lands_p.append(l)
                    dfs(i, j, l)


        return lands_p
