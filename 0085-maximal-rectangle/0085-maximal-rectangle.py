from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        ans = 0

        for r in range(rows):

            # Build histogram
            for c in range(cols):
                if matrix[r][c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0

            # Largest rectangle in histogram
            stack = [-1]

            for i in range(cols + 1):
                curr = heights[i] if i < cols else 0

                while stack[-1] != -1 and heights[stack[-1]] >= curr:
                    h = heights[stack.pop()]
                    width = i - stack[-1] - 1
                    ans = max(ans, h * width)

                stack.append(i)

        return ans