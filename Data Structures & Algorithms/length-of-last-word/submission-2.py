class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        t = s.rstrip().lstrip()
        new = t.split(" ")
        return len(new[-1])