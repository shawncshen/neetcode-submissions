class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #current
        #remaining
        #start
        result = []
        def backtrack(start, current, remaining):
            if remaining == 0:
                result.append(current.copy()) #why copy?
                return
            if remaining < 0: #is this when we need to keep adding?
                return
            for index in range(start, len(nums)):
                number = nums[index]
                current.append(number)
                backtrack(index, current, remaining - number) #idk what this means
                current.pop() #why pop?
        backtrack(0, [], target)
        return result