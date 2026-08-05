class Solution:
    def isLucky(self, n): 
        #code here
        return self.check(n,2)
        
        
    def check(self,n, counter):
        
        if counter > n:
            return True 
        
        if n % counter == 0:
            return False
            
        n = n - (n//counter)
        
        return self.check(n,counter+1)
