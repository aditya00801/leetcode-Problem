class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0 
        for x in nums:
            xor ^= x

        # if total  xor is non zero 
        # the  entire array  is the ans 
        if xor != 0:
            return len(nums)
        
        # If all elements are zero, no valid subsequence exists.
        if all(x ==0 for x in nums):
            return 0
        
        return len(nums) - 1