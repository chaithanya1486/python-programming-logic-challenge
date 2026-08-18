class Solution:
    def rearrange(self, arr, x):
        a = []
        for num in arr:
            diff = abs(num - x)
            a.append((diff, num))
        a.sort(key=lambda item: item[0])
        for i in range(len(arr)):
            arr[i] = a[i][1]
        return arr
