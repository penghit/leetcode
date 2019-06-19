class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if not needle:
            return 0
        
        nlen = len(needle)
        if haystack[0:nlen] == needle:
            return 0
        
        for i in range(len(haystack) - nlen + 1):
            if haystack[i:i+nlen] == needle:
                return i
        
        return -1
