class Solution:
    def binaryGap(self, N: int) -> int:
        max = 0

        current = None
        for i in range(32):
            if N & (1 << i):
                if current and current > max:
                    max = current
                current = 1
            elif current:
                current += 1

        return max
