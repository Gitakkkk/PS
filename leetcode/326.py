# 326. Power of Three

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        if n<=0 or n%3!=0:
            return False
        return Solution.isPowerOfThree(self,n//3)