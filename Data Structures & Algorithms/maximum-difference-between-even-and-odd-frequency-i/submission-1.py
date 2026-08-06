class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+= 1
        odd = (i for i in freq.values() if i%2!=0)
        even = (j for j in freq.values() if j%2==0)

        return max(odd) - min(even)            