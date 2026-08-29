from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []

        # Preserve original order
        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)

        ans = []

        # Positive must come first
        for i in range(len(positive)):
            ans.append(positive[i])
            ans.append(negative[i])

        return ans