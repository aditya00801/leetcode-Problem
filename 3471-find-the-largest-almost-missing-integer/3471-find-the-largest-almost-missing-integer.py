from typing import List
from collections import defaultdict

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = defaultdict(set)  # num -> set of subarray indices

        # Step 1: generate all subarrays of size k
        for i in range(n - k + 1):
            sub = nums[i:i+k]
            for num in sub:
                count[num].add(i)  # record subarray index

        # Step 2: filter those appearing in exactly one subarray
        candidates = [num for num, subs in count.items() if len(subs) == 1]

        # Step 3: return largest or -1
        return max(candidates) if candidates else -1
