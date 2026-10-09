class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def ruleOne():
            # Rule 1 
            for row in range(len(board)):
                valid = set()
                for num in board[row]:
                    if num != ".":
                        if num in valid:
                            return False
                        valid.add(num)
            return True

        def ruleTwo():
            # Rule 2
            for col in range(len(board[0])):
                valid = set()
                for element in range(len(board)):
                    if board[element][col] != ".":
                        if board[element][col] in valid:
                            return False
                        valid.add(board[element][col])
            return True

        def ruleThree(box):
            valid = set()
            for row in range(3):
                for col in range(3):
                    if box[row][col] != ".":
                        if box[row][col] in valid:
                            return False
                        valid.add(box[row][col])
            return True

        if not ruleOne() or not ruleTwo():
            return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                sub_box = [row[j:j+3] for row in board[i:i+3]]
                if not ruleThree(sub_box):
                    return False

        return True
