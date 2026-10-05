class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        left=0
        set1=set()
        for right in range(len(s)):
            while s[right] in set1:
                set1.remove(s[left])
                left=left+1
            set1.add(s[right])
            max_len=max(max_len,right-left+1)
                
        return max_len

        