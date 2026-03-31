class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Goal : return False if duplicate. return True if pass all 3 conditions

        # condition 1: Check row duplicate
        for row in board:
            rowSet = set()
            for val in row:
                if val == '.':
                    continue
                elif val in rowSet:
                    return False
                rowSet.add(val)

        # condition 2: Check col duplicate
        for col in range(9):
            colSet = set()
            for row in range(9):
                if board[row][col] == '.':
                    continue
                elif board[row][col] in colSet:
                    return False
                colSet.add(board[row][col])

        # condition 3: Check 3x3 by row/col divide by 3 to get coordinate
        square = collections.defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                key = (row // 3, col // 3)
                if board[row][col] in square[key]:
                    return False
                square[key].add(board[row][col])

        # Passed all conditions
        return True

        