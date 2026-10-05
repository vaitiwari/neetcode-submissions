class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        sub_set=set()
        left=0
        for right in range(len(s)):
            while s[right] in sub_set:
                sub_set.remove(s[left])
                left=left+1
            sub_set.add(s[right])
            max_len=max(max_len,right-left+1)
        return max_len