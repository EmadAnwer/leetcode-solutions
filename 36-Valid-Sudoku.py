class Solution(object):
    def isValidSudoku(self, board):
        \\\
        :type board: List[List[str]]
        :rtype: bool
        \\\
        def isValid(nums):
            nums = [i for i in nums if i != '.']
            return len(set(nums)) == len(nums)
        for i in range(9):
            if not isValid(board[i]):
                return False
            if not isValid([board[j][i] for j in range(9)]):
                return False
            if not isValid([board[i//3*3+j//3][i % 3*3+j % 3] for j in range(9)]):
                return False
        return True