class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        

        """
        [3,7,8]
        [9,11,13]
        [15,16,17]
        
        """

        res = []
        for i in range(len(matrix)):
            min_n = 100001
            min_n_idx = -1
            for j in range(len(matrix[i])):
                if min_n > matrix[i][j]:
                    min_n_idx = j
                    min_n = matrix[i][j]
            
            max_n = 0
            for j in range(len(matrix)):
                if max_n < matrix[j][min_n_idx]:
                    max_n = matrix[j][min_n_idx]

            if min_n == max_n:
                res.append(max_n)


        return res
