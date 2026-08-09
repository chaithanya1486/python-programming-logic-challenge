class Solution:

    def reverseInGroups(self, arr, k):
        """code here"""
        n = len(arr)
        start = 0

        while start < n:
            end = min(start + k - 1, n - 1)

            left = start
            right = end

            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

            start += k
