def solution(n):
    i = 1
    fa = 1
    while fa <= n:
        i += 1
        fa *= i
    return i - 1