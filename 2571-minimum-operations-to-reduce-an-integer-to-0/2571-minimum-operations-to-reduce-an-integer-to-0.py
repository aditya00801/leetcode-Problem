class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0

        while n > 0:
            if n & 1:
                # If n % 4 == 1, subtract 1
                if n == 1 or n % 4 == 1:
                    n -= 1
                else:
                    # n % 4 == 3 → add 1
                    n += 1

                ans += 1

            else:
                n //= 2

        return ans