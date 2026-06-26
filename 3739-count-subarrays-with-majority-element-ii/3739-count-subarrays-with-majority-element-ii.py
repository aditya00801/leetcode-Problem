from typing import List


class FenwickTree:
    def __init__(self, size: int):
        # 1-indexed Fenwick tree
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index: int, delta: int) -> None:
        # Add `delta` at position `index`
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index: int) -> int:
        # Returns sum of frequencies in range [1..index]
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        """
        Optimized solution.

        Transform:
            nums[i] == target -> +1
            nums[i] != target -> -1

        Then count subarrays with positive sum.

        Let prefix[i] be the prefix sum up to i.
        For each current prefix `p`, we need the number of previous prefixes
        strictly less than `p`.

        Since prefix sums can be negative, we coordinate-compress them and use
        a Fenwick Tree to maintain frequencies of seen prefix sums.
        """

        n = len(nums)

        # Step 1: Build all prefix sums
        prefix_sums = [0]
        running_sum = 0

        for value in nums:
            if value == target:
                running_sum += 1
            else:
                running_sum -= 1
            prefix_sums.append(running_sum)

        # Step 2:
        # Prefix sums can be negative and very large.
        # Replace each unique prefix sum with its position in sorted order so that can be used as indices in the Fenwick Tree.
        sorted_unique = sorted(set(prefix_sums))
        rank = {value: i + 1 for i, value in enumerate(sorted_unique)}  # 1-indexed

        # Step 3: Fenwick tree to count frequencies of prefix sums seen so far
        fenwick = FenwickTree(len(sorted_unique))

        answer = 0

        # Initially we have seen prefix sum 0 once
        fenwick.update(rank[0], 1)

        # Step 4: Process each prefix sum after index 0
        for i in range(1, len(prefix_sums)):
            current_prefix = prefix_sums[i]
            current_rank = rank[current_prefix]

            # Every previous prefix sum that is smaller than the current one forms a subarray with a positive sum.
            answer += fenwick.query(current_rank - 1)

            # Add current prefix sum to the data structure
            fenwick.update(current_rank, 1)

        return answer      