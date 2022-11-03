class Solution:
    def strStr(self, haystack, needle):
        needle_length = len(needle)
        haystack_length = len(haystack)
        
        if needle_length > haystack_length:
            return -1
        
        if needle_length == 0:
            return 0
        
        for i in range(haystack_length - needle_length + 1):
            if haystack[i:i + needle_length] == needle:
                return i
            
        return -1