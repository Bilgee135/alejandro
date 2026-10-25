class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = [] # keeps track of evals
        operators = "+-*/"
        
        def helper(token):
            right = operands.pop()
            left = operands.pop()
            if token == "+":
                operands.append(left + right)
            elif token == "-":
                operands.append(left - right)
            elif token == "*":
                operands.append(left * right)
            elif token == "/":
                operands.append(int(left / right))

        for token in tokens:
            if token in operators: # Fixed search so fast enough
                helper(token)
            else:
                operands.append(int(token))

        return operands[-1]