from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        for i in range(len(s2) - len(s1) + 1):
            window = s2[i:window_size + i]
            if Counter(window) == Counter(s1):
                return True
        return False
