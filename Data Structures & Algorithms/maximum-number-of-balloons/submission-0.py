class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashmap = {}

        for i in text:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1

        new = []

        for letter in "balon":
            count = hashmap.get(letter, 0)

            if letter == "l" or letter == "o":
                new.append(count // 2)
            else:
                new.append(count)

        return min(new)