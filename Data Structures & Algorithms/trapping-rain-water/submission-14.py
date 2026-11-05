class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        stack = [] # keeps track of empty spaces in between bars
                    # (start, i)
        total = 0

        L = 0
        while height[L] == 0:
            L += 1
        
        R = L + 1
        while R < len(height):
            if height[R] < height[L]:
                stack.append((L, R))
                R += 1
                continue
            while stack and height[L] <= height[R]:
                start, i = stack.pop()
                total += height[start] - height[i]
            L = R
            R += 1
        
        next_tall = 0
        while stack:
            start, i = stack.pop()
            if i == len(height) - 1:
                continue

            if height[i+1] >= next_tall:
                next_tall = height[i + 1] 

            if height[i] < next_tall:
                total += min(height[start], next_tall) - height[i]

        return total   


