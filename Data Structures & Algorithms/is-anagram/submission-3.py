class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #cant use set because t can only compare unique characters
        
        return sorted(s) == sorted(t)