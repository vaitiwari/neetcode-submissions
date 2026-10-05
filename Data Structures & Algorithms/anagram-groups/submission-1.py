class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_list=[]
        dict1=defaultdict(list)
        for i in strs:
            sorted_word="".join(sorted(i))
            dict1[sorted_word].append(i)
        return list(dict1.values())


        



        