class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        slow = 0 
        fast = 1
        profit = 0
        while fast < len(prices):
            temp_profit = prices[fast] - prices[slow]
            if temp_profit > 0:
                profit = max(profit, temp_profit)
            else:
                slow = fast
            fast += 1
        return profit