class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                result = 1
                for j in range(1, len(needle)):
                    haystack_index = i + j
                    if haystack_index >= len(haystack):
                        break
                    if haystack[haystack_index] == needle[j]:
                        result += 1
                if result == len(needle):
                    return i 
        return -1