from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        if window_size > len(s1):
            return False

        target = Counter(s1)
        counts = Counter(s2[:window_size])

        if counts == target:
            return True

        for i in range(1, len(s2) - len(s1) + 1):
            counts[s2[i - 1]] -= 1
            counts[s2[i + window_size -1]] +=1
            if counts == target:
                return True
        return False