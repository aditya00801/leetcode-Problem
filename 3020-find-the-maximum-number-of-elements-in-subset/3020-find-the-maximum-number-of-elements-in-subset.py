from collections import Counter

class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        count = Counter(nums)
        result = 0

        # Special case: x = 1 -> [1,1,1,...] must be odd length
        ones = count.get(1, 0)
        if ones:
            result = ones if ones % 2 == 1 else ones - 1

        for x in count:
            if x == 1:
                continue

            pairs, cur = 0, x
            while count.get(cur, 0) >= 2:
                pairs += 1
                nxt = cur * cur
                if nxt > 10**9:
                    cur = nxt
                    break
                cur = nxt

            if count.get(cur, 0) >= 1:
                result = max(result, 2 * pairs + 1)
            elif pairs > 0:
                result = max(result, 2 * (pairs - 1) + 1)
            else:
                result = max(result, 1)

        return result