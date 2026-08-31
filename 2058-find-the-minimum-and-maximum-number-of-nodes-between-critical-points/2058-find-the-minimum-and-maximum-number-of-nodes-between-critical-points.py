# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first = -1
        prev = -1
        minDist = float('inf')

        left = head
        cur = head.next
        pos = 1

        while cur.next:
            right = cur.next

            # Local maximum or local minimum
            if ((cur.val > left.val and cur.val > right.val) or
                (cur.val < left.val and cur.val < right.val)):

                if first == -1:
                    first = pos
                else:
                    minDist = min(minDist, pos - prev)

                prev = pos

            left = cur
            cur = right
            pos += 1

        # Fewer than two critical points
        if first == prev:
            return [-1, -1]

        maxDist = prev - first

        return [minDist, maxDist]