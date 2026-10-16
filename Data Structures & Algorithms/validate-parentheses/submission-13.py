class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openCloseMap = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for c in s:
            if c in openCloseMap:
                if stack and stack[-1] == openCloseMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0