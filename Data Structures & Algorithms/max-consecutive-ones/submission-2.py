class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_val = 0
        for num in nums:
            if num == 1:
                counter += 1
            else:
                if max_val < counter:
                    max_val = counter
                counter = 0
        if max_val < counter:
            max_val = counter
        return max_val