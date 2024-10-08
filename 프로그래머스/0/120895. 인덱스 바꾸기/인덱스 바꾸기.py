def solution(my_string, num1, num2):
    sl = list(my_string)
    sl[num1], sl[num2] = sl[num2], sl[num1]
    return ''.join(sl)