from collections import Counter

def solution(a, b, c, d):
    count = Counter([a, b, c, d])
    values = list(count.values())
    keys = list(count.keys())
    
    if 4 in values:
        return 1111 * keys[0]
    
    elif 3 in values:
        p = keys[values.index(3)]  # 세 번 나온 숫자
        q = keys[values.index(1)]  # 한 번 나온 숫자
        return (10 * p + q) ** 2
    
    elif values.count(2) == 2:
        p, q = keys
        return (p + q) * abs(p - q)
    
    elif 2 in values and 1 in values:
        p = keys[values.index(2)]  # 두 번 나온 숫자
        q, r = [key for key, val in count.items() if val == 1]  # 한 번 나온 두 숫자
        return q * r
    
    else:
        return min(a, b, c, d)
