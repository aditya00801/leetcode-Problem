class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:

        MOD = 10**9 + 7

        # Total number of possible values
        m = r - l + 1

        # Base Case:
        # For arrays of length 1, every value can be chosen once.
        dp = [1] * m

        # Build DP for lengths 2 to n
        for length in range(2, n + 1):

            # Reverse the DP array.
            # This converts the required suffix sums into prefix sums.
            dp.reverse()

            # Running prefix sum
            prefix = 0

            # Update DP in-place
            for i in range(m):

                # Save the current value before overwriting it
                current = dp[i]

                # New DP value = sum of all previous values
                dp[i] = prefix

                # Update running prefix sum
                prefix = (prefix + current) % MOD

        # Sum all valid ending states.
        # Multiply by 2 because the DP counts only one direction
        # (Up → Down). The opposite direction (Down → Up)
        # contributes the same number of arrays.
        return (sum(dp) * 2) % MOD