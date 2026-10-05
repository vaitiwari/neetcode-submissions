from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1=Counter(nums)
        dict1=dict(sorted(dict1.items(), key= lambda x:x[1], reverse=True))
        list1=[]
        counter=0
        for key in list(dict1.keys()):
            if counter<k:
                list1.append(key)
                counter=counter+1
        
        return list1