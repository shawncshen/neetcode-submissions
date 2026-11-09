class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        longest_length = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            length = right - left + 1
            max_freq = max(count.values())
            replacement_needed = length - max_freq

            
            while replacement_needed > k:
                count[s[left]] -= 1
                left += 1
                length = right - left + 1
                max_freq = max(count.values())
                replacement_needed = length - max_freq
            longest_length = max(longest_length, length)
        return longest_length