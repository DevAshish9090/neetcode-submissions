class Solution:
    def scoreOfString(self, s: str) -> int:
        c = [ord(i) for i in s]
        i = 0 
        total = 0 
        while i < len(c)-1:
            total = total + (abs(c[i+1]- c[i]))
            i = i+1
        return total     
