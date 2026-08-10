class Solution:
    def findMean(self, arr):
        # code here 
        sums = sum(arr)
        x = sums // len(arr)
        return x
