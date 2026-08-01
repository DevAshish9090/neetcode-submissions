class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0 
        count = 0 
        while i < len(s)-1:
            count = count + abs(ord(s[i+1])- ord(s[i]))
            i = i +1
        return count    
