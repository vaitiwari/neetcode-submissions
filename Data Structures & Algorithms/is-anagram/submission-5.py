class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for char in s:
            if char not in t or (s.count(char)!=t.count(char)):
                return False
            if len(s)!=len(t):
                return False
        return True
        