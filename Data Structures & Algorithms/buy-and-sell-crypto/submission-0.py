class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        max=-999999999
        for i in range(n):
            for j in range(i+1, n):
                if prices[j]-prices[i]>max:
                    max=prices[j]-prices[i]
        if max<0:
            max=0
        return max
        