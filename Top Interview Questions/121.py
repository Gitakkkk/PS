# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        small = float('inf')
        ans = 0
        for price in prices:
            if price < small: small = price
            elif price - small > ans: ans = price - small
        return ans