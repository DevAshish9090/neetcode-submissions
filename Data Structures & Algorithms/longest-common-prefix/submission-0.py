class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        base = strs[0]

        if strs == " ":
            return ""

        for i in range(len(base)):
            for word in strs[1:]:
                if i>= len(word) or word[i] != base[i]:
                    return result
            else:
                result = result + base[i]



        return result