class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        str1=""
        while i<len(word1) or j<len(word2):
            if i<len(word1):
                str1=str1+word1[i]
            if j<len(word2):
                str1=str1+word2[j]
            i=i+1
            j=j+1
        # str1=str1+word1[i:]
        # str1-str1+word2[j:]
        return str1