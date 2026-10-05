class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        buy=0
        max_profit=0
        for index1 in range(len(prices)):
            buy=prices[index1]
            for index2 in range(index1+1,len(prices)):
                profit=prices[index2]-buy
                if profit>max_profit:
                    max_profit=profit
        return max_profit


        