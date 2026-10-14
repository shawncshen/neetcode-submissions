class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for str in strs:
            key = "".join(sorted(str))
            #if new is in one of store, add it in that one. else add to new one.
            if key in store:
                store[key].append(str)
            else:
                store[key] = [str]
        return list(store.values())
