class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in details:
            if int(i[11:13])>60:
                count = count+1
        return count    
            
                  