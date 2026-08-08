class Solution:
	def removeVowels(self, s):
		# code here
		ans = ""
		for i in range(len(s)):
		    if s[i] not in "aeiou":
		        ans+=s[i]
		return ans
