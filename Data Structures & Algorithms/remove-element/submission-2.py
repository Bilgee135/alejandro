class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        def helper(index):
            for j in range(index+1, len(nums)):
                nums[j-1] = nums[j]
            nums[len(nums) - 1] = None

        counter = 0

        for i, n in enumerate(nums):
            while nums[i] == val:
                helper(i)
                counter += 1

        k = len(nums) - counter
        return k
            

        