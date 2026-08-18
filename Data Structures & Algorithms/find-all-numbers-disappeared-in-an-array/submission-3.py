class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Use the array itself as a hash map:
        # for each value x, mark index (x-1) as "seen" by negating it
        for x in nums:
            idx = abs(x) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        
        # any index still positive means (index + 1) never appeared
        missing = [i + 1 for i in range(n) if nums[i] > 0]
        
        # restore the original array (good practice, avoids side effects)
        for i in range(n):
            nums[i] = abs(nums[i])
        
        return missing