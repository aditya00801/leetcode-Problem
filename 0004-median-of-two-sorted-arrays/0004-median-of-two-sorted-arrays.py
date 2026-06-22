class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        # Always binary search on the smaller array
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        # Total number of elements
        total = len(A) + len(B)

        # Number of elements needed in left partition
        half = (total + 1) // 2

        # Binary search range on smaller array
        l, r = 0, len(A)

        while l <= r:

            # Partition index in A
            i = (l + r) // 2

            # Partition index in B
            j = half - i

            # Elements around partition
            Aleft  = float('-inf') if i == 0 else A[i - 1]
            Aright = float('inf')  if i == len(A) else A[i]

            Bleft  = float('-inf') if j == 0 else B[j - 1]
            Bright = float('inf')  if j == len(B) else B[j]

            # Valid partition condition:
            # All left elements <= all right elements
            if Aleft <= Bright and Bleft <= Aright:

                # Odd length → median is max of left side
                if total % 2:
                    return max(Aleft, Bleft)

                # Even length → average of middle two values
                return (
                    max(Aleft, Bleft) +
                    min(Aright, Bright)
                ) / 2

            # Too many elements taken from A
            elif Aleft > Bright:
                r = i - 1

            # Too few elements taken from A
            else:
                l = i + 1