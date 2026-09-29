class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in tracker:
                return [tracker[diff], i]

            tracker[n] = i
            