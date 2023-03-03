# 942. DI String Match
# permutation을 array로 해석. perm은 각 요소.
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        result = []
        min = 0
        max = len(s)
        for i, x in enumerate(s):
            if x == 'I':
                result.append(min)
                min+=1
            else:
                result.append(max)
                max-=1
        result.append(min)
        return result