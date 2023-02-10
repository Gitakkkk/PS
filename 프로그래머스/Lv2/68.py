def solution(s):
    count = 0
    for x in s:
        if x == '(':
            count+=1
        else:
            if count == 0: return False
            count-=1
    return count == 0