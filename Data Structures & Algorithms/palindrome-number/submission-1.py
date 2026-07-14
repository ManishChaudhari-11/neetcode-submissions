class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = abs(x)
        rev = 0

        while num > 0:
            rev = rev * 10 + num % 10
            num //= 10

        if rev <= (-(2**31)) or rev >= (2**31 - 1):
            return False

        return rev == x
