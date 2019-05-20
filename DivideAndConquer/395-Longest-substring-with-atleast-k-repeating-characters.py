class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # a dictornay holding the number of times a char appears
        cntdic = {}
        
        for char in s:
            if char in cntdic:
                cntdic[char] += 1
            else:
                cntdic[char] = 1
                
        #an easier way to accomplish the following work is
        #cntdic = Collections.Counter(s)
        
        # characters that appears less than k times which shouldn't appear in the sub
        # string and so should be seperated 
        separator = [char for char in cntdic if cntdic[char] < k]
        print(separator)
        if not separator:
            return len(s)
        
        subs = re.split('|'.join(separator), s)
        
        return max(self.longestSubstring(t, k) for t in subs)
        
        
