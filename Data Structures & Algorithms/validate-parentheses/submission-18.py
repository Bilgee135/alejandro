class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }

        for p in s:
            if p in close_open:
                if stack and stack[-1] == close_open[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)

        return len(stack) == 0