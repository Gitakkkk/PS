def solution(s):
    count = 0
    _del = 0
    
    while s != '1':
        # s 문자열에 '0'이 포함됨
        if '0' in s:
            # '0'의 개수 누산
            _del += s.count('0')
            s = s.replace('0', '')
        # s문자열을 2진법으로 변환, '#b'에서 '#'을 빼면 접두어 제거됨
        s = format(len(s), 'b')
        count += 1
        
    return [count, _del]