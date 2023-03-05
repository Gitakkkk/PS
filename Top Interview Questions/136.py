# 136. Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for x in nums:
            if x in dic: del dic[x]
            else: dic[x] = 1
        for key in dic:
            return key