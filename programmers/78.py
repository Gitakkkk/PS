def solution(n, m, section):
    answer = 1
    # 칠한 벽
    a = section[0]
    
    for idx in range(1, len(section)):
        if (section[idx] - a >= m):
            a = section[idx]
            answer += 1
        
    return answer