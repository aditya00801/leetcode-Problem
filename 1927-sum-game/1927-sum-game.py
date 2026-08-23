class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        sum1 = sum2 = q1 = q2 = 0

        for i in range(half):
            if num[i] == '?':
                q1 += 1
            else:
                sum1 += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                q2 += 1
            else:
                sum2 += int(num[i])

        total_q = q1 + q2
        if total_q % 2 == 1:
            return True  # Alice always makes the last move

        # Bob's forced final difference under optimal pairing strategy
        return (sum1 - sum2) + 9 * (q1 - q2) // 2 != 0