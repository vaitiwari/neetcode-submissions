class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag=False
        for i in nums:
            if nums.count(i)>1:
                return True  
        return flag
         