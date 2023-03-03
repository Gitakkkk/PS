# 860. Lemonade Change

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        s = {"5": 0, "10": 0}
        for x in bills:
            if x == 5:
                s["5"] += 1
            elif x == 10:
                s["10"] += 1
                s["5"] -= 1
                if 0 > s["5"]: return False
            else:
                if s["10"] <= 0:
                    if s["5"] < 3: return False
                    s["5"] -= 3
                else:
                    if s["5"] < 1: return False
                    s["10"] -= 1
                    s["5"] -= 1
        return True