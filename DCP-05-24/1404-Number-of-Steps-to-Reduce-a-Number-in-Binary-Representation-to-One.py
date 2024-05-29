class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)  # Convert binary string to integer
        steps = 0

        while num != 1:
            if num % 2 == 0:
                num //= 2  # Divide by 2 if the number is even
            else:
                num += 1  # Add 1 if the number is odd
            steps += 1

        return steps