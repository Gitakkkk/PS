# 387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        idx_dic = {}
        ele_dic = {}
        for i in range(len(s)):
            if s[i] not in idx_dic: idx_dic[s[i]] = i
        for x in s:
            if x not in ele_dic: ele_dic[x] = 1
            else: ele_dic[x] += 1
        for ele_key, ele_value in ele_dic.items():
            if ele_value == 1:
                for idx_key, idx_value in idx_dic.items():
                    if ele_key == idx_key: return idx_value
        return -1
