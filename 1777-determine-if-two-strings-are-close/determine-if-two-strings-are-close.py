from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1, counter2 = Counter(word1), Counter(word2)
        # print(counts1 == counts2)
        # print(counter1.values(), counter2.values())
        # if counter1 == counter2 and counter1.values() == counter2.values():
        # if (counter1 == counter2) or (counter1.values() == counter2.values()):
        # if counter1.values() == counter2.values():
        if (counter1.keys() == counter2.keys()) and (sorted(counter1.values()) == sorted(counter2.values())):
            return True
        return False