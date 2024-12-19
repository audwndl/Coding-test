def solution(quiz):
    answer = []
    for i in quiz:
        j,k = i.split(' = ')
        if eval(j) == int(k):
            answer.append("O")
        else :
            answer.append("X")
    return answer