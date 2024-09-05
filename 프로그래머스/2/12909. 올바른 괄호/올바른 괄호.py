def solution(s):
    temp = []
    for i in s:
        if i=="(":
            temp.append(i)
        else:
            if not temp:
                return False
            else:
                temp.pop()
    if temp:
        return False
    else:
        return True