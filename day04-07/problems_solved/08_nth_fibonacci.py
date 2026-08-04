class Solution:
    def nthFibonacci(self, n):
        # Code here
        if n == 0:
            return n
        elif n == 1:
            return n
        else :
            return self.nthFibonacci(n-1) + self.nthFibonacci(n-2)
