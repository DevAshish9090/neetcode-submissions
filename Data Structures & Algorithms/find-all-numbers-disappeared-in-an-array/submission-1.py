class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        k = set(list(nums))
        missing = []
        for i in range(1,n+1):
            if i not in k:
                missing.append(i)
        return missing        