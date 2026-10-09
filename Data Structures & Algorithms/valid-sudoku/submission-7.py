class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = set()
                
        def ruleOne():
            # Rule 1 
            for row in range(len(board)):
                valid.clear()
                for num in board[row]:
                    if num != ".":
                        if num in valid:
                            return False
                        valid.add(num)

            valid.clear()
            return True

        def ruleTwo():
            # Rule 2
            for col in range(len(board[0])):
                valid.clear()
                for element in range(len(board)):
                    if board[element][col] != ".":
                        if board[element][col] in valid:
                            return False
                        valid.add(board[element][col])

            valid.clear()
            return True

        def ruleThree(box):
            for row in range(3):
                for col in range(3):
                    if box[row][col] != ".":
                        if box[row][col] in valid:
                            return False
                        valid.add(box[row][col])

            valid.clear()
            return True

        if not ruleOne() or not ruleTwo():
            return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                sub_box = [row[j:j+3] for row in board[i:i+3]]
                if not ruleThree(sub_box):
                    return False

        return True
