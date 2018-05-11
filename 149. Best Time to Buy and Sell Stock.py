class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if prices == []:
            return 0
        else:
            b = prices[0]
            max_profit = 0
            for i in range(1, len(prices)):
                b = min(b, prices[i])
                max_profit = max(max_profit, prices[i] - b)
            return max_profit