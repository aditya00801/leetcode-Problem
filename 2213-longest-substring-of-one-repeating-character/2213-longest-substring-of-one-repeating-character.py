class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)

        # Each node stores:
        # [left_char, right_char, length, prefix, suffix, best]

        tree = [None] * (4 * n)

        def merge(a, b):
            left_char = a[0]
            right_char = b[1]

            length_a = a[2]
            length_b = b[2]

            prefix_a = a[3]
            suffix_a = a[4]
            best_a = a[5]

            prefix_b = b[3]
            suffix_b = b[4]
            best_b = b[5]

            prefix = prefix_a
            suffix = suffix_b
            best = max(best_a, best_b)

            # Characters at the boundary are the same
            if a[1] == b[0]:

                # Join suffix of left + prefix of right
                best = max(best, suffix_a + prefix_b)

                # Entire left segment has the same character
                if prefix_a == length_a:
                    prefix = length_a + prefix_b

                # Entire right segment has the same character
                if suffix_b == length_b:
                    suffix = suffix_a + length_b

            return [
                left_char,
                right_char,
                length_a + length_b,
                prefix,
                suffix,
                best
            ]

        def build(node, l, r):
            if l == r:
                tree[node] = [
                    s[l],  # left character
                    s[l],  # right character
                    1,     # length
                    1,     # prefix
                    1,     # suffix
                    1      # best
                ]
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, index, char):
            if l == r:
                tree[node] = [
                    char,
                    char,
                    1,
                    1,
                    1,
                    1
                ]
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, r, index, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        answer = []

        for char, index in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, index, char)
            answer.append(tree[1][5])

        return answer