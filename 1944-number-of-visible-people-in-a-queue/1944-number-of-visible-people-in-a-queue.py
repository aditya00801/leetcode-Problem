from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = [0] * n
        stack = []  # will store indices of people to the right
        
        for i in range(n - 1, -1, -1):  # traverse from right to left
            count = 0
            while stack and heights[i] > heights[stack[-1]]:
                stack.pop()
                count += 1
            if stack:  # if someone taller remains
                count += 1
            answer[i] = count
            stack.append(i)
        
        return answer
