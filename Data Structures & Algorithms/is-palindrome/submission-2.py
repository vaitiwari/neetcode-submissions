class Solution:
    def isPalindrome(self, s: str) -> bool:
        # str1=("".join(s.split()))
        # str2=("".join(s.split()))[::-1]

        s1 = re.sub(r'[^a-zA-Z0-9]', '', s)

        left, right=0,len(s1)-1
        while left<right:
            if s1[left].lower()!=s1[right].lower():
                return False
            left=left+1
            right=right-1
        return True
            
        # s2=re.sub(r'[^a-zA-Z0-9]', '', str2)
        # print(s1)
        # print(s2)
        # if s1.lower()==s2.lower():
        #     return True
        # else:
        #     return False


        