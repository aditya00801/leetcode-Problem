from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        def is_valid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1

                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = deque([s])
        visited = {s}
        result = []

        found = False

        while queue:

            for _ in range(len(queue)):
                current = queue.popleft()

                # Check whether current string is valid
                if is_valid(current):
                    result.append(current)
                    found = True

                # Don't generate strings with more removals
                if found:
                    continue

                # Remove one parenthesis
                for i in range(len(current)):

                    if current[i] not in "()":
                        continue

                    next_string = current[:i] + current[i + 1:]

                    if next_string not in visited:
                        visited.add(next_string)
                        queue.append(next_string)

            # First valid BFS level = minimum removals
            if found:
                break

        return result

        