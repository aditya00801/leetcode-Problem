class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        # Left pass: answer[i] = product of all elements before i
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        # Right pass: multiply in product of all elements after i
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer
