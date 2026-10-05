from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter=Counter(s1)
        left=0
        right=len(s1)-1
        s2_counter=Counter(s2[0:len(s1)])
        while right<len(s2)-1:
            if s2_counter==s1_counter:
                return True
            else:
                s2_counter[s2[left]]=s2_counter.get(s2[left],0)-1
                s2_counter[s2[right+1]]=s2_counter.get(s2[right+1],0)+1
                left=left+1
                right=right+1
            # tem_str=s2[i:i+len(s1)]
            # if Counter(tem_str)==s1_counter:
            #     return True
        return s2_counter==s1_counter