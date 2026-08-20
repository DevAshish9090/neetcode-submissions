class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        N = n*n
        freq = [0] * (N+1)  # [0,0,0,0,0]

        for i in grid:
            for j in i:
                freq[j] += 1   #[0,1,2,1,0]

        missing = 0
        repeated = 0        
        
        for i in range(1,N+1):
            if freq[i] == 2:
                repeated = i
            elif freq[i] == 0:
                missing = i
        return([repeated,missing])            