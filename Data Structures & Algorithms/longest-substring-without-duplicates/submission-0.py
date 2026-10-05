class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        max_val=0
        myset=set()
        for right in range(len(s)):
            while s[right] in myset:
                myset.remove(s[left])
                left=left+1
            myset.add(s[right])
            max_val=max(max_val,right-left+1)
        return max_val

            


        