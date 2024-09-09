def solution(s):
    answer = [0,0]
    while int(s)>1:
        answer[0] += 1 # 회차
        answer[1] += s.count("0") # 제거할 0의 개수
        s = format(s.count("1"), 'b') # s의 개수를 2진수로 변환 : format(value, 'b')
    return answer