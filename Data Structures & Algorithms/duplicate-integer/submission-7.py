class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        copy = [] #i am creating a empty list here.
        for i in nums: #traverse through each number in nums
            if i  in copy: 
                return True
            else:
                copy.append(i)
        return False
        