class Solution:
    def getMinMax(self, arr):
        # code here
        min = arr[0]
        max = arr[0]
        for i in range(1,len(arr)):
            if arr[i] > max :
                max = arr[i]
            if arr[i] < min:
                min = arr[i]
        return min, max
