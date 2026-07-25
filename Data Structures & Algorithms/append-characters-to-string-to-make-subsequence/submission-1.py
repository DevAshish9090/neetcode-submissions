class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        new = ""
        i = 0 
        for j in range(len(s)):
            if i<len(t) and s[j] == t[i]:
                i = i+1
        new = t[i:]
        return len(new) 