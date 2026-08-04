class Solution:

    def fib(self, n):

        if n == 0:
            return 0

        if n == 1:
            return 1

        return self.fib(n-1) + self.fib(n-2)

    def fibonacciNumbers(self, n):

        ans = []

        for i in range(n):
            ans.append(self.fib(i))

        return ans
