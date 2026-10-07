class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [], [None] * len(nums)
        product, output = 1, []

        # prefix products
        for num in nums:
            product *= num
            prefix.append(product)
        
        product = 1
        # postfix products
        for i in range(len(nums)-1, -1, -1):
            product *= nums[i]
            postfix[i] = product

        # products of array
        for i in range(len(nums)):
            left = prefix[i-1] if i > 0 else 1
            right = postfix[i+1] if i < len(nums)-1 else 1
            output.append(left * right)

        return output