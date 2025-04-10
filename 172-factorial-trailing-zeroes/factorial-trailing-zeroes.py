class Solution:
    def trailingZeroes(self, n: int) -> int:
        countTrailingZero = 0
        i = 5
        while n // i >= 1:
            countTrailingZero += n // i
            i *= 5
        return countTrailingZero

        