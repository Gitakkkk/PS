# 2144. Minimum Cost of Buying Candies With Discount

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        result = 0
        cost.sort(reverse=True)
        idx = 2
        for i, x in enumerate(cost):
            if i == idx:
                idx += 3
                continue
            result += x
        return result