from typing import List

class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n
        ans = []
        count = 0
        
        for index, color in queries:
            # remove old contribution
            if colors[index] != 0:
                if index > 0 and colors[index] == colors[index - 1]:
                    count -= 1
                if index < n - 1 and colors[index] == colors[index + 1]:
                    count -= 1
            
            # update color
            colors[index] = color
            
            # add new contribution
            if index > 0 and colors[index] == colors[index - 1]:
                count += 1
            if index < n - 1 and colors[index] == colors[index + 1]:
                count += 1
            
            ans.append(count)
        
        return ans
