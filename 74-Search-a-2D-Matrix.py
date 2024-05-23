class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        l, r = 0 ,len(matrix) -1

        m = (l + r) // 2

        row = -1
        while l <= r:
            if matrix[m][-1] >=  target and matrix[m][0] <=  target:
                row = m
                break
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                r = m - 1

            m = (l + r) // 2

        if row != -1:
            l, r = 0 ,len(matrix[row]) -1
            m = (l + r) // 2

            while l <= r:

                if matrix[row][m] == target:
                    return True
                elif matrix[row][m] > target:
                    r = m - 1
                else:
                    l = m + 1

                m = (l + r) // 2


        return False