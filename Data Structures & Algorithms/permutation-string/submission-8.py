from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter=Counter(s1)
        for i in range(len(s2)-len(s1)+1):
            tem_str=s2[i:i+len(s1)]
            if Counter(tem_str)==s1_counter:
                return True
        return False