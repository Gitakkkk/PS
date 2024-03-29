# 70. Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n

        steps = [0, 1, 2, 3]

        for i in range(4, n+1):
            steps.append(steps[i-1] + steps[i-2])

        return steps.pop()