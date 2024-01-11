class Solution:
    def minTimeToType(self, word: str) -> int:
        result = 0
        initial = 'a'
        for i in range(len(word)):
            # ord: 하나의 문자를 받고 그 문자에 해당하는 유니코드 정수 반환
            # abs: 절대값 반환
            # 유니코드 값을 통해 앞으로 갈지, 뒤로 갈지 결정
            diff = abs(ord(word[i])-ord(initial))
            # diff==뒤로 간다, 26-diff==앞으로 간다
            result += min(diff, 26-diff)
            result += 1
            initial = word[i]
        return result