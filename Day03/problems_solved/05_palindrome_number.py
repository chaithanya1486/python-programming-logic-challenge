class Solution:
    def isPalindrome(self, n):
        n = abs(n)
        y = n
        x = 0

        while y > 0:
            a = y % 10
            x = x * 10 + a
            y //= 10

        return x == n
