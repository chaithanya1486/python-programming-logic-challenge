class Solution:

    def lessThan(self, arr, k):
        #code here
        x = []
        for i in range(len(arr)):
            if arr[i] < k:
                x.append(arr[i])
        return x
