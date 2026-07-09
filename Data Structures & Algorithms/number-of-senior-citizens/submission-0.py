class Solution:
    def countSeniors(self, details: List[str]) -> int:
        new = []
        count = 0
        for i in details:
            new.append(int(i[11:13]))
        for j in new:
            if j>60:
                count = count+1
        return count
            
                  