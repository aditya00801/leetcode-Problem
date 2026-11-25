class Solution(object):
    def smallestUniqueSubarray(self, nums):
        n = len(nums)

        MOD1 = 10**9 + 7
        MOD2 = 10**9 + 9
        BASE = 911382323

        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)

        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)

        for i in range(n):
            pow1[i + 1] = pow1[i] * BASE % MOD1
            pow2[i + 1] = pow2[i] * BASE % MOD2

            h1[i + 1] = (h1[i] * BASE + nums[i]) % MOD1
            h2[i + 1] = (h2[i] * BASE + nums[i]) % MOD2

        def check(k):
            count = {}

            for i in range(n - k + 1):
                hash1 = (h1[i + k] - h1[i] * pow1[k]) % MOD1
                hash2 = (h2[i + k] - h2[i] * pow2[k]) % MOD2

                key = (hash1, hash2)
                count[key] = count.get(key, 0) + 1

            return any(freq == 1 for freq in count.values())

        low = 1
        high = n

        while low <= high:
            mid = low + (high - low) // 2

            if check(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low