def solution(name, yearning, photo):
    answer = []
    
    for i in range(len(photo)):
        rating = 0
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                index = name.index(photo[i][j])
                rating += yearning[index]
        answer.append(rating)
    
    return answer