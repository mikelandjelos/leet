class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) < 2:
            return 0

        max_profit = 0
        sell = 1
        buy = 0

        while sell < len(prices):
            profit = prices[sell] - prices[buy]

            if profit > max_profit:
                max_profit = profit

            if profit <= 0:
                buy = sell

            sell += 1

        return max_profit
