class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # monotonic non-decreasing

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, last = stack.pop()
                maxArea = max(maxArea, last * (i - index))
                start = index
            stack.append((start, h))

        while stack:
            index, h = stack.pop()
            maxArea = max(maxArea, h * (len(heights) - index))
        
        return maxArea
