import numpy as np

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        grid = np.array(grid)
        vals,counts = np.unique(grid,return_counts=True)
        all_values = np.arange(1,grid.shape[1]**2+1)
        
        dup = np.array([val for val,count in zip(vals,counts) if count>1])
        repeated = np.setdiff1d(all_values, grid)[0]

        return [dup[0],repeated]
        #return 
