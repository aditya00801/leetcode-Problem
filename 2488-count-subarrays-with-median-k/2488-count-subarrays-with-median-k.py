from typing import List
from collections import defaultdict


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        pos = nums.index(k)

        # Count balances on the left of k
        count = defaultdict(int)
        balance = 0

        count[0] = 1

        for i in range(pos - 1, -1, -1):
            if nums[i] > k:
                balance += 1
            else:
                balance -= 1

            count[balance] += 1

        # Extend to the right, including k
        ans = 0
        balance = 0

        for i in range(pos, len(nums)):

            if nums[i] > k:
                balance += 1
            elif nums[i] < k:
                balance -= 1

            # Odd length  -> balance = 0
            # Even length -> balance = 1
            ans += count[-balance]
            ans += count[1 - balance]

        return ans