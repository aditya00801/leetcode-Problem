class Solution:
    def maxProduct(self, root):
        MOD = 10**9 + 7

        # Step 1: Calculate total sum
        def get_sum(node):
            if not node:
                return 0

            return node.val + get_sum(node.left) + get_sum(node.right)

        total = get_sum(root)

        # Step 2: Find the best split
        best = 0

        def dfs(node):
            nonlocal best

            if not node:
                return 0

            subtree_sum = (
                node.val
                + dfs(node.left)
                + dfs(node.right)
            )

            product = subtree_sum * (total - subtree_sum)
            best = max(best, product)

            return subtree_sum

        dfs(root)

        return best % MOD
        