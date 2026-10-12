class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(list(set(nums)))
        if len(nums) == 1:
            return 1

        lenMap = defaultdict(int)
        start = 0

        for i in range(len(nums)-1):
            if nums[i] - nums[i+1] < -1:
                lenMap[tuple(nums[start:i+1])] = len(nums[start:i+1])
                start = i + 1

            if i+1 == len(nums)-1:
                lenMap[tuple(nums[start:])] = len(nums[start:])

        return max(lenMap.values())