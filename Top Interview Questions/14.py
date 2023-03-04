# 14. Longest Common Prefix

# 내가 작성한 코드
# dic 형태에 값 저장은 했지만 최대 개수의 key들을 못 뽑아냄
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        _dic = {}
        ans = ''

        for i in range(len(strs)):
            for x in strs[i]:
                if x in _dic: _dic[x] += 1
                else: _dic[x] = 1
        
        print(_dic)
        return ans

# 다른 사람이 작성한 코드
# 앞에서부터 확인하면 되는 문제였음
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for x in zip(*strs):
            if len(set(x)) == 1:
                ans += x[0]
            else:
                return ans
        return ans
                        