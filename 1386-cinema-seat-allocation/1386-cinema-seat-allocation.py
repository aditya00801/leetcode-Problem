from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        rows = defaultdict(set)

        # Store reserved seats row-wise
        for row, seat in reservedSeats:
            rows[row].add(seat)

        ans = 0

        # Rows with no reservations can always fit 2 families
        ans += (n - len(rows)) * 2

        for seats in rows.values():

            left = {2, 3, 4, 5}
            middle = {4, 5, 6, 7}
            right = {6, 7, 8, 9}

            if not (seats & left) and not (seats & right):
                # Both sides are available
                ans += 2

            elif not (seats & left) or not (seats & middle) or not (seats & right):
                # At least one valid group can fit
                ans += 1

        return ans