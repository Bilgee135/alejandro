class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set('+-*/') # fast lookup
        operands = [] # stack

        def evaluate(token):
            right = operands.pop()
            left = operands.pop()
            val = 0
            if token == '+':
                val = left + right
            elif token == '-':
                val = left - right
            elif token == '*':
                val = left * right
            elif token == '/':
                val = int(left / right)
            
            operands.append(val)

        for token in tokens:
            if token in operators:
                evaluate(token)
            else:
                operands.append(int(token))

        return operands[-1] 