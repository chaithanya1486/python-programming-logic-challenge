class Solution:
    def sumOfDigits(self, n):
        # code here
        sum = 0
        temp = n
        while temp > 0:
            x = temp % 10
            sum +=x
            temp//=10
        return sum
