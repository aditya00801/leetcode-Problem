class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        m = len(nums2)

        # dp[i][j] = maximum dot product using
        # nums1[0:i] and nums2[0:j]
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                product = nums1[i - 1] * nums2[j - 1]

                # Take both elements as a pair.
                take = product

                # Extend a previously formed subsequence.
                if dp[i - 1][j - 1] != float('-inf'):
                    take = max(
                        take,
                        dp[i - 1][j - 1] + product
                    )

                # Skip nums1[i - 1]
                skip1 = dp[i - 1][j]

                # Skip nums2[j - 1]
                skip2 = dp[i][j - 1]

                dp[i][j] = max(take, skip1, skip2)

        return dp[n][m]