class Solution:
    def replaceElements(self, num: List[int]) -> List[int]:

        for i in range (len(num)-1):
            num[i] = max(num[i+1:])
        num[-1] = -1
        return num    
        