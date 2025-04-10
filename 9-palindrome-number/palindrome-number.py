class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringOfX = str(x)
        return stringOfX == stringOfX[::-1]
