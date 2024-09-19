def solution(n):
    li = [1,2]
    if n==1:
        return 1
    for i in range(2, n):
        li.append(li[i-1]+li[i-2])
    return li[-1]%1234567
    '''
    1-1
    2-2
    3-3
    4-5
    5-8
    손으로 그리면서 숫자 세봄.
    결과는 앞의 두개의 수를 더한것 - 피보나치수열
    '''