class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for str in strs:
            while not str.startswith(prefix):
                prefix = prefix[:-1]
        
        return prefix