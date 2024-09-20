import math
def solution(arr):      
    answer = 1
    for i in arr:
        answer = (i * answer) // math.gcd(i, answer)
    return answer

'''
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a
'''
