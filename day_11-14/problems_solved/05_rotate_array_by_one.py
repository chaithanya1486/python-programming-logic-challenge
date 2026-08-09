class Solution:
    def rotate(self, arr):
        return arr.insert(0, arr.pop())
