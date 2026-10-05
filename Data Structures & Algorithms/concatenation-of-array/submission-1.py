class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        sns=[]
        for i in range(2):
            sns=sns+nums
        return sns        