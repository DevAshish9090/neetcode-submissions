class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = {}

        for i in text:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1

        new = []

        for i in "balon":
            count = hashmap.get(i, 0)

            if i == "l" or i == "o":
                new.append(count // 2)
            else:
                new.append(count)

        return min(new)