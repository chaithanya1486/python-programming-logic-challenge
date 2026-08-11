class Solution:
    def countOccurence(self, arr, k):
        b = {}

        for x in arr:
            if x in b:
                b[x] += 1
            else:
                b[x] = 1

        count = 0

        for x in b:
            if b[x] > len(arr) / k:
                count += 1

        return count
        
