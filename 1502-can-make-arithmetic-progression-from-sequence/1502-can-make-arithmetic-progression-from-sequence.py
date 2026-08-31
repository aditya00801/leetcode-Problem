class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        if len(arr) < 2:
            return False
        arr = sorted(arr)
        d = arr[0] - arr[1]

        for i in range(1, len(arr)):
            if arr[i-1] - arr[i] != d:
                return False
        
        return True
