from collections import deque
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        target = n - 1

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        weights = set()

        for u, v, w in edges:
            graph[u].append((v, w))
            indegree[v] += 1
            weights.add(w)

        # Topological Sort
        q = deque(i for i in range(n) if indegree[i] == 0)
        topo = []

        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        INF = float("inf")

        def check(limit):
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                if u != 0 and u != target and not online[u]:
                    continue

                cur = dist[u]

                for v, w in graph[u]:
                    if w < limit:
                        continue
                    if v != target and v != 0 and not online[v]:
                        continue

                    nd = cur + w
                    if nd < dist[v]:
                        dist[v] = nd

            return dist[target] <= k

        # No path exists
        if not check(0):
            return -1

        vals = sorted(weights)

        lo, hi = 0, len(vals) - 1
        ans = 0

        while lo <= hi:
            mid = (lo + hi) // 2

            if check(vals[mid]):
                ans = vals[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        return ans