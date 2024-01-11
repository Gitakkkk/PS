def solution(n):
    n_cnt = format(n, 'b').count('1')
    temp = n + 1
    while True:
        if format(temp, 'b').count('1') == n_cnt: return temp
        temp += 1