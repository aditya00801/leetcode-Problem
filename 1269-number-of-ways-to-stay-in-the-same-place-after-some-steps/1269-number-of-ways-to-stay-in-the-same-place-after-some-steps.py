class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7

        # We can never reach beyond `steps`
        size = min(arrLen, steps + 1)

        # dp[i] = number of ways to be at index i
        dp = [0] * size
        dp[0] = 1

        for _ in range(steps):
            new_dp = [0] * size

            for i in range(size):
                # Stay
                new_dp[i] += dp[i]

                # Move left
                if i > 0:
                    new_dp[i] += dp[i - 1]

                # Move right
                if i + 1 < size:
                    new_dp[i] += dp[i + 1]

                new_dp[i] %= MOD

            dp = new_dp

        return dp[0]