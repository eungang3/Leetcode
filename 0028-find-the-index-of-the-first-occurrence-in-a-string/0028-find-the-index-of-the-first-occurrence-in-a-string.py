class Solution:
    def strStr(self, haystack, needle):
        needle_length, haystack_length = len(needle), len(haystack)
        if needle_length == 0:
            return needle_length
        if haystack_length < needle_length:
            return -1
        for i in range(haystack_length - needle_length + 1):
            if haystack[i:i + needle_length] == needle:
                return i
        return -1