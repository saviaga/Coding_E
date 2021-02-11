class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = collections.defaultdict(list)
        for elem in strs:
                ans[tuple(sorted(elem))].append(elem)
        return ans.values()
        