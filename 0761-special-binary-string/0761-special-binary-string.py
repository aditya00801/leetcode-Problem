class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        parts = []
        balance = 0
        start = 0

        for i, ch in enumerate(s):
            if ch == '1':
                balance += 1
            else:
                balance -= 1

            # Found one complete special substring
            if balance == 0:
                inner = s[start + 1:i]

                # Recursively maximize the inside
                best_inner = self.makeLargestSpecial(inner)

                # Add 1 and 0 back
                parts.append('1' + best_inner + '0')

                start = i + 1

        # Put larger special substrings first
        parts.sort(reverse=True)

        return ''.join(parts)