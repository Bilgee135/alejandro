class Solution:
    def trap(self, height: List[int]) -> int:
        # Cannot contain water
        if len(height) < 3:
            return 0

        # Keeps track of empty spaces
        stack = [] 
        total = 0

        # Beginning zeros are not considered
        L = 0
        while L < len(height) and height[L] == 0:
            L += 1
        
        # Process heights from left
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
        
        # Process remaining heights from right
        next_tall = 0
        while stack:
            start, i = stack.pop()
            if i == len(height) - 1:
                continue

            if height[i+1] >= next_tall:
                next_tall = height[i + 1] 

            if height[i] < next_tall:
                total += next_tall - height[i]

        return total   


