
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        cur = 1

        for i in range(1, len(arr)):
            if arr[i] >= cur + 1:
                cur += 1

        return cur