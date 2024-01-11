# 350. Intersection of Two Arrays II

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap,result = {},[]
        for num in nums1:hashMap[num] = hashMap.get(num,0)+1
        for num in nums2:
            if num in hashMap and hashMap[num] != 0:
                result.append(num) 
                hashMap[num] -= 1
        return result 