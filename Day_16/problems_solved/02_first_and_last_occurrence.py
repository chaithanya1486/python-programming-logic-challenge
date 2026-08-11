class Solution:
    def find(self, arr, x):
        # code here
        first = -1
        last = -1
        for i in range(len(arr)):
            if arr[i] == x:
                if first == -1:
                    first = i
                last = i
        return first, last
