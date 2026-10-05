class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        def ispalidrome(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                else:
                    l=l+1
                    r=r-1
            return True
        while left<right:
            if s[left]!=s[right]:
                return ispalidrome(left+1,right) or ispalidrome(left,right-1) 
            left=left+1
            right=right-1
        return True
                