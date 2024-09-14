def solution(s): 
    a = []
    for i in s:
        if not a:
            a.append(i)
        elif a[-1] == i:
            a.pop()
        else: 
            a.append(i)
    if not a: 
        return 1
    else: 
        return 0 