class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        n = int(len(nums))

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] = hashmap[i] + 1

        for i, j in hashmap.items():
            if j > (n / 2):
                return i 