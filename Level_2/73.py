def solution(s):
    arr = list(s)
    stack = []
    for i in arr:
        if len(stack) == 0: stack.append(i)
        elif stack[-1] == i: stack.pop()
        else: stack.append(i)
    if len(stack) == 0: return 1
    return 0