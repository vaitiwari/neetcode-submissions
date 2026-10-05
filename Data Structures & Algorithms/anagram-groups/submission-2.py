class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_list=[]
        dict1={}
        for i in strs:
            sorted_word="".join(sorted(i))
            if sorted_word in dict1:
                dict1[sorted_word].append(i)
            else:
                dict1[sorted_word]=[i]
        print(dict1)
        return list(dict1.values())


        



        