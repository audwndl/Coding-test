def solution(slice, n):
    pizza = 1
    while not pizza*slice >= n:
        pizza += 1
    return pizza