from typing import List

class Solution:
    def lexicographicallySmallestArray(
        self, nums: List[int], limit: int
    ) -> List[int]:

        n = len(nums)

        # (value, original index)
        arr = [(nums[i], i) for i in range(n)]
        arr.sort()

        ans = nums[:]

        left = 0

        while left < n:
            right = left

            # Find the connected component
            while (
                right + 1 < n
                and arr[right + 1][0] - arr[right][0] <= limit
            ):
                right += 1

            # Values are already sorted
            values = [arr[i][0] for i in range(left, right + 1)]

            # Get original indices and sort them
            indices = [arr[i][1] for i in range(left, right + 1)]
            indices.sort()

            # Smallest values go to smallest original indices
            for i in range(len(values)):
                ans[indices[i]] = values[i]

            left = right + 1

        return ans