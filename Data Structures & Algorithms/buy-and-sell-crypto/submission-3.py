class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        max_sum=0
        while right<=len(prices)-1:
            if prices[right]>prices[left]:
                max_sum=max(max_sum,prices[right]-prices[left])
            else:
                left=right
            right=right+1
        
        return max_sum
