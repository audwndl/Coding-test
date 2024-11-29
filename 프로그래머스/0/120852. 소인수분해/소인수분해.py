def solution(n):
    answer = []
    a = 2
    while a*a <= n:
        while n % a == 0: 
            if a not in answer:
                answer.append(a)
            n //= a
        a += 1
    if n>1:
        answer.append(n)
    return answer