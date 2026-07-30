class Solution:
    def kthDigit(self, a, b, k):
        # code here
        x = a**b
        for i in range(k-1):
            x = x//10
        return x%10
            
