from typing import List

class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        n = len(nums)
        mx = max(nums)

        # Smallest Prime Factor
        spf = list(range(mx + 1))

        for p in range(2, int(mx ** 0.5) + 1):
            if spf[p] == p:
                for x in range(p * p, mx + 1, p):
                    if spf[x] == x:
                        spf[x] = p

        # DSU
        parent = list(range(n))
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            a = find(a)
            b = find(b)

            if a == b:
                return

            if size[a] < size[b]:
                a, b = b, a

            parent[b] = a
            size[a] += size[b]

        # Connect indices having a common prime factor
        first = {}

        for i, num in enumerate(nums):
            x = num

            while x > 1:
                p = spf[x]

                if p in first:
                    union(i, first[p])
                else:
                    first[p] = i

                while x % p == 0:
                    x //= p

        # Compare with sorted array.
        # Handle duplicate values using queues of original indices.
        from collections import defaultdict, deque

        positions = defaultdict(deque)

        for i, x in enumerate(nums):
            positions[x].append(i)

        sorted_nums = sorted(nums)

        for i, x in enumerate(sorted_nums):
            original_index = positions[x].popleft()

            if find(i) != find(original_index):
                return False

        return True

        