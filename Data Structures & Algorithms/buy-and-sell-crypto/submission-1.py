class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        min_val=99999999999
        max_val=-9999999999
        for i in prices:
            if i < min_val:
                min_val=i
            elif i-min_val>max_val:
                max_val=i-min_val
        if max_val <0:
            max_val=0
        return max_val
        