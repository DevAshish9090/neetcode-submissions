class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = {}
        new = []
        
        for i in range(1, n + 1):
            freq[i] = 0
            
        for num in nums:
            freq[num] = 1
            
        for i, j in freq.items():
            if freq[i] == 0:
                new.append(i)
                
        return new