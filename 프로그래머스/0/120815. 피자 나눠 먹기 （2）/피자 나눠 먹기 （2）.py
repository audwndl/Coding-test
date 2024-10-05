def solution(n):
    pizza = 1
    while not pizza*6%n==0:
        pizza+=1
    return pizza