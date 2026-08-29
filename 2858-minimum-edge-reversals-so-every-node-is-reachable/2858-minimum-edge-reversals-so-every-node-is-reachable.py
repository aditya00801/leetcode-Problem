from typing import List

class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:

        graph = [[] for _ in range(n)]

        for u, v in edges:
            # Original direction: u -> v
            graph[u].append((v, 0))

            # Going v -> u requires reversal
            graph[v].append((u, 1))

        ans = [0] * n

        # -------------------------------------------------
        # DFS 1:
        # Calculate answer[0]
        # -------------------------------------------------
        def dfs1(u, parent):
            for v, cost in graph[u]:
                if v == parent:
                    continue

                ans[0] += cost
                dfs1(v, u)

        dfs1(0, -1)

        # -------------------------------------------------
        # DFS 2:
        # Reroot answer from u -> v
        # -------------------------------------------------
        def dfs2(u, parent):
            for v, cost in graph[u]:
                if v == parent:
                    continue

                if cost == 0:
                    # Original edge: u -> v
                    ans[v] = ans[u] + 1
                else:
                    # Original edge: v -> u
                    ans[v] = ans[u] - 1

                dfs2(v, u)

        dfs2(0, -1)

        return ans