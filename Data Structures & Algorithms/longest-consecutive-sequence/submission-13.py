class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(list(set(nums)))
        if len(nums) == 1:
            return 1

        maxLen = 0
        start = 0

        for i in range(len(nums)-1):
            if nums[i] - nums[i+1] < -1:
                maxLen = max(maxLen, i+1 - start)
                start = i + 1
            if i+1 == len(nums)-1:
                maxLen = max(maxLen, len(nums) - start)

        return maxLen