class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_end = min_end = result = nums[0]
        
        for n in nums[1:]:
            candidates = (n, max_end * n, min_end * n)
            max_end = max(candidates)
            min_end = min(candidates)
            result = max(result, max_end)
        
        return result