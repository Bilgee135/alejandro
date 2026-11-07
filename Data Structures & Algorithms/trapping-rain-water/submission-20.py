class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        stack = [] # Height to process
        L = 0 
        while L < len(height) and height[L] == 0:
            L += 1
        R = L + 1
        while R < len(height):
            if height[L] > height[R]:
                stack.append(R)
                R += 1
                continue
            while stack and height[L] <= height[R]:
                index = stack.pop()
                total += height[L] - height[index]
            L = R
            R += 1
        right_h = 0 
        while stack:
            index = stack.pop()
            if index == len(height) - 1:
                continue
            if height[index + 1] >= right_h:
                right_h = height[index + 1]
            if height[index] < right_h:
                total += right_h - height[index]
        return total


