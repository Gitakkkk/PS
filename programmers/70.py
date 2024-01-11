def solution(n):
    count = 0
    for i in range(1,n+1):
        tempi = i
        tempn = n
        while True:
            tempn -= tempi
            if tempn == 0:
                count += 1
                break
            elif tempn < 0:
                break
            tempi += 1
    return count