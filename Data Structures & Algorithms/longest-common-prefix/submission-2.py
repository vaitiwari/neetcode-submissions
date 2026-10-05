class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base=strs[0]
        common=""
        for word in strs[1:]:
            while not word.startswith(base):
                base=base[:-1]
                if not base:
                    return ""
            
        return base

                    