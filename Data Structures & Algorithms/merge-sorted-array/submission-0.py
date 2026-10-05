class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        result=[]
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                result.append(nums1[i])
                i=i+1
            else:
                result.append(nums2[j])
                j=j+1
        result=result+nums1[i:m]
        result=result+nums2[j:n]
        nums1[:]=result
