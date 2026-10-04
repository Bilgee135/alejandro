class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        preSum = []
        preTotal = 0
        for num in nums:
            preTotal += num
            preSum.append(preTotal)

        for i in range(len(nums)):
            leftSum = preSum[i-1] if i > 0 else 0
            rightSum = (preSum[len(nums)-1] - preSum[i]) 
            if leftSum == rightSum:
                return i

        return -1 