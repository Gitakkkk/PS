# 내가 작성한 답
# return 부분에서 헤맴
def solution(n, words):
    dic = {}
    dic[words[0]] = 1
    for i in range(1, len(words)):
        if words[i] in dic:
            i += 1
            if i <= n: return [i, i % n]
            else: return [i // n, n % i]
        else: dic[words[i]] = 1
        if words[i-1][-1] != words[i][0]:
            i += 1
            if i <= n: return [i, i % n]
            else: return [i // n, i % n]
    return [0, 0]

# 다른 사람이 작성한 답
# dic 새로 만들어서 저장 X, (i%n)+1, (i//n)+1 방법으로 정답 Return
def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i] :
            return [(i%n)+1, (i//n)+1]
    else:
        return [0,0]