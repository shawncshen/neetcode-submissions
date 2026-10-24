class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            length = len(s)
            encoded_string += str(length) + "#"+ s
        return encoded_string
# 5#hello5#world
    def decode(self, s: str) -> List[str]:
        my_list = []
        i = 0
        while i < len(s):
            j = s.find("#", i) #1
            start = j + 1
            length = int(s[i:j]) #prints 5
            end = start + length
            word = s[start:end]
            my_list.append(word)
            i = end

        return my_list