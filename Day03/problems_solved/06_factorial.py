class Solution:
    def factorial(self, n: int) -> int:
        # code here
        fact = 1
        i = 1
        while i <=n:
            fact = fact * i
            i+=1
        return fact
