class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # Initialize the matrix with zeros
        matrix = [[0] * len(colSum) for _ in range(len(rowSum))]
        
        # Traverse through each cell of the matrix
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                value = min(rowSum[i], colSum[j])
                
                matrix[i][j] = value
                
                rowSum[i] -= value
                colSum[j] -= value
                
        return matrix