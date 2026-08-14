from collections import defaultdict

class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        n = len(parent)
        graph = [[] for _ in range(n)]
        
        # Build adjacency list
        for i in range(1, n):
            graph[parent[i]].append(i)
        
        # DFS to compute masks
        masks = [0] * n
        def dfs(node, mask):
            masks[node] = mask
            for child in graph[node]:
                c = ord(s[child]) - ord('a')
                dfs(child, mask ^ (1 << c))
        
        dfs(0, 0)
        
        # Count pairs
        freq = defaultdict(int)
        ans = 0
        for mask in masks:
            # Case 1: same mask
            ans += freq[mask]
            
            # Case 2: differ by one bit
            for b in range(26):
                ans += freq[mask ^ (1 << b)]
            
            freq[mask] += 1
        
        return ans
