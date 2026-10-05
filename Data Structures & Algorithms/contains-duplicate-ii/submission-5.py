class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        set1=set()
        left=0

        for right in range(len(nums)):
            if right - left >k:
                set1.remove(nums[left])
                left += 1
            if nums[right] in set1:
                return True
            set1.add(nums[right])
        return False
