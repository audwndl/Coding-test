def solution(l, r):
    answer=[]
    for i in range(l, r+1):
        #all() 함수는 문자열의 모든 문자(c)가 "0" 또는 "5"인 경우에만 True를 반환
        if all(num in '05' for num in str(i)):
            answer.append(i)
    if not answer:
        return [-1]
    return answer