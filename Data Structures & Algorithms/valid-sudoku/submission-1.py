class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = {}
                
        def ruleOne(matrix):
            # Rule 1 
            for row in range(len(matrix)):
                valid.clear()
                for num in matrix[row]:
                    if num != ".":
                        if num in valid:
                            return False
                        valid[num] = 1

            valid.clear()
            return True

        def ruleTwo(matrix):
            # Rule 2
            for col in range(len(matrix[0])):
                valid.clear()
                for element in range(len(matrix)):
                    if matrix[element][col] != ".":
                        if matrix[element][col] in valid:
                            return False
                        valid[matrix[element][col]] = 1

            valid.clear()
            return True

        def ruleThree(box):
            seen = set()
            for r in range(3):
                for c in range(3):
                    val = box[r][c]
                    if val != ".":
                        if val in seen:
                            return False
                        seen.add(val)
            return True

        if not ruleOne(board) or not ruleTwo(board):
            return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                sub_box = [row[j:j+3] for row in board[i:i+3]]
                if not ruleThree(sub_box):
                    return False

        return True
