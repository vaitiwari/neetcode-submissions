class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        min_len=len(nums)+1
        left=0
        tmp_sum=0

        for right in range(len(nums)):
            tmp_sum=tmp_sum+nums[right]
            while tmp_sum>=target:
                min_len=min(min_len,right-left+1)
                tmp_sum=tmp_sum-nums[left]
                left=left+1
        if min_len==len(nums)+1:
            return 0
        return min_len
