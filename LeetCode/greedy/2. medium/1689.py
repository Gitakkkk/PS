# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
# 내가 작성한 코드.
class Solution:
    def minPartitions(self, n: str) -> int:
        arr = list(map(int, n))
        return max(arr)
# 남이 작성한 코드 중 괜찮은 코드.
class Solution:
    def minPartitions(self, n: str) -> int:
        for i in ['9','8','7','6','5','4','3','2','1','0']:
            if i in n:
                return int(i)