class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1=("".join(s.split()))
        str2=("".join(s.split()))[::-1]

        s1 = re.sub(r'[^a-zA-Z0-9]', '', str1)
        s2=re.sub(r'[^a-zA-Z0-9]', '', str2)
        print(s1)
        print(s2)
        if s1.lower()==s2.lower():
            return True
        else:
            return False


        