class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        # Check rows and columns
        for i in range(9):
            row = [False] * 9
            col = [False] * 9

            for j in range(9):
                # Check row
                if board[i][j] != ".":
                    if row[ord(board[i][j]) - ord("1")]:
                        return False
                    row[ord(board[i][j]) - ord("1")] = True
                
                # Check column
                if board[j][i] != ".":
                    if col[ord(board[j][i]) - ord("1")]:
                        return False
                    col[ord(board[j][i]) - ord("1")] = True

        # Check 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [False] * 9
                for k in range(3):
                    for l in range(3):
                        if board[i + k][j + l] != ".":
                            if box[ord(board[i + k][j + l]) - ord("1")]:
                                return False
                            box[ord(board[i + k][j + l]) - ord("1")] = True

        return True