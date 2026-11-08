class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        chars = set()
        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            length = right - left + 1
            max_length = max(max_length, length)
        return max_length