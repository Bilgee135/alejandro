class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}

        for i, n in enumerate(nums):
            if target-n in tracker:
                return [tracker[target-n], i]

            tracker[n] = i
            