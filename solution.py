class Solution:
    def binaryGap(self, N: int) -> int:
        n = [*bin(N)][2:]
        max = 0

        current = 0
        for num in n:
            if num == '1':
                if current > max:
                    max = current
                current = 1
            else:
                current += 1

        return max
