class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        front = right + 1
        back = n - left
        both = (left + 1) + (n - right)

        return min(front, back, both)