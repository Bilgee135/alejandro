class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(list(set(nums)))
        maxLen = 0
        start = 0

        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > 1:
                maxLen = max(maxLen, i+1 - start)
                start = i + 1

        return max(maxLen, len(nums) - start)