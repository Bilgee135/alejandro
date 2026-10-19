class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # monotonic non-decreasing
        nextWarmer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                # Next warmer day is at index i
                warmerIdx = stack.pop()

                # Add the day difference to nextWarmer
                nextWarmer[warmerIdx] = i - warmerIdx
            stack.append(i)

        return nextWarmer