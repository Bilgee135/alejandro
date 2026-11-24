class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area, stack = 0, []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = max(area, height * (i - index))
                start = index
            stack.append((start, h))

        while stack:
            i, h = stack.pop()
            area = max(area, h * (len(heights) - i))

        return area