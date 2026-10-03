class NumArray:

    def __init__(self, nums: List[int]):
        self.sum = []
        total = 0
        for num in nums:
            total += num
            self.sum.append(total)

    def sumRange(self, left: int, right: int) -> int:
        sumRight = self.sum[right]
        sumLeft = self.sum[left-1] if left > 0 else 0
        return (sumRight - sumLeft)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)