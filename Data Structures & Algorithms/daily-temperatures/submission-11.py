class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [] # Next greater - monotonic non-increasing stack

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                top = stack.pop()
                ans[top] = i - top
            stack.append(i)
        
        return ans