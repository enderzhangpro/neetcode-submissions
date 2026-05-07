class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def containsDuplicates(nine):
            new_nine = []
            for i in nine:
                if i != '.':
                    new_nine.append(i)
            return len(set(new_nine)) != len(new_nine)
        
        # get rows
        for row in board:
            if containsDuplicates(row):
                return False
        
        # get columns
        for i in range(9):
            column = []
            for j in range(9):
                column.append(board[j][i])
            if containsDuplicates(column):
                return False
        # get three by threes
        for i in range(0, 9, 3):
            for k in range(0, 9, 3):
                box = []
                for j in range(i, i + 3):
                    for l in range(k, k + 3):
                        box.append(board[j][l])
                if containsDuplicates(box):
                    return False
        return True