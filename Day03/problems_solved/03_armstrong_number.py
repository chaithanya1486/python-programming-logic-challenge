class Solution:
    def armstrongNumber (self, n):
        # code here 
        x = n  
        c = 0
        while x > 0:
            c+=1
            x=x//10
        x= n 
        t= 0
        while x > 0:
            y = x%10
            t+= y**c
            x//=10
        if t == n:
             return True
        else :
            return False
