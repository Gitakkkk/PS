# 1323. Maximum 69 Number
class Solution:
    def maximum69Number (self, num: int) -> int:
        result = num
        nums = list(str(num))
        for i in range(len(nums)):
            if nums[i] == '6':
                nums[i] = '9'
                temp = ''.join(nums)
                if int(temp) > result:
                    result = int(temp)
                nums[i] = '6'
        return result