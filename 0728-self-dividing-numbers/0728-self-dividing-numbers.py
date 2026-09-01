class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []

        for num in range(left, right + 1):
            original = num
            temp = num
            valid = True

            while temp > 0:
                digit = temp % 10

                # Digit 0 is not allowed
                if digit == 0:
                    valid = False
                    break

                # Number must be divisible by every digit
                if original % digit != 0:
                    valid = False
                    break

                temp //= 10

            if valid:
                ans.append(original)

        return ans