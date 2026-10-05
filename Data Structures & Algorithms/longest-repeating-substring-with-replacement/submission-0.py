class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter={}
        left=0
        max_len=0
        max_freq=0

        for right in range(len(s)):
            counter[s[right]]=counter.get(s[right],0)+1
            max_freq=max(counter[s[right]],max_freq)
            if (right-left+1)-max_freq> k:
                counter[s[left]]=counter.get(s[left],0)-1
                left=left+1
            if counter[s[left]]<1:
                counter.remove[s[left]]
            max_len=max(max_len,right-left+1)
        return max_len