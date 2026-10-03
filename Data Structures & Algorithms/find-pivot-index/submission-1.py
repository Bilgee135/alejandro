class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        preSum = []
        postSum = [None] * len(nums)
        preTotal = 0
        postTotal = 0

        for num in nums:
            preTotal += num
            preSum.append(preTotal)

        for i in range(len(nums)-1, -1, -1):
            postTotal += nums[i]
            postSum[i] = postTotal

        for i in range(len(nums)):
            strictLeft = preSum[i-1] if i > 0 else 0
            strictRight = postSum[i+1] if i < len(nums)-1 else 0 
            if strictLeft == strictRight:
                return i
                
        return -1 