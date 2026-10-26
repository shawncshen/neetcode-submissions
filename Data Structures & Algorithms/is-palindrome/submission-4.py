class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            #expression to check for isalnum?
            if not s[start].isalnum():
                start += 1
                continue 
            if not s[end].isalnum():
                end -= 1
                continue
            if s[start].lower() != s[end].lower(): 
                return False

            if s[start].lower() == s[end].lower(): 
                start += 1 
                end -= 1
            
        return True
            
            
        