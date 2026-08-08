class Solution:
    def reverseWords(self, s):
        words = s.split(".")

        ans = []

        for word in words:
            if word != "":
                ans.append(word)

        ans.reverse()

        return ".".join(ans)
