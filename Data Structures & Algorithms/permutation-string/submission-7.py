from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:len(s1)])
        
        for i in range(len(s1), len(s2)):
            if s1_counter == s2_counter:
                return True
            
            # add new right char
            s2_counter[s2[i]] += 1
            
            # remove left char
            left_char = s2[i - len(s1)]
            s2_counter[left_char] -= 1
            if s2_counter[left_char] == 0:
                del s2_counter[left_char]  # keep counter clean
        
        return s1_counter == s2_counter