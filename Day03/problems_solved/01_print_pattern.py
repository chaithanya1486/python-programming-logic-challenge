class Solution:
    def pattern(self, n):
        ans = []
        current = n

        while current > 0:
            ans.append(current)
            current -= 5

        while current <= n:
            ans.append(current)
            current += 5

        return ans
