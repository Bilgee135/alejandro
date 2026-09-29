class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}

        for i, n in enumerate(nums):
            if target-n not in tracker:
                tracker[n] = i
            else:
                return [tracker[target-n], i]

            
            