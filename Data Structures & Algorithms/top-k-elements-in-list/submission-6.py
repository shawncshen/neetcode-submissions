class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for i in nums:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in dictionary.items():
            buckets[freq].append(num)
        result = []
        for i in range(len(buckets) -1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
            