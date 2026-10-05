class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst=[]
        for i , num in enumerate(nums):
            if target-num in nums[i+1:]:
                lst.append(i) 
                lst.append(nums.index(target-num,i+1))
                return lst

        