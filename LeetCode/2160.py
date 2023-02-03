# 2160. Minimum Sum of Four Digit Number After Splitting Digits

class Solution:
    def minimumSum(self, num: int) -> int:
        nums = sorted(list(str(num)))
        a = int(nums[0] + nums[2])
        b = int(nums[1] + nums[3])
        return a + b