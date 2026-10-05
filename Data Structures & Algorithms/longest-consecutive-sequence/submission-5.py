class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        list1=list(sorted(set(nums)))
        if list1 ==[]:
            return 0
        counter=1
        print(list1)
        max=1
        for i in range (0,len(list1)-1):
            if list1[i]+1==list1[i+1]:
                counter=counter+1
            else:
                counter=1
            if counter>max:
                max=counter
        return max