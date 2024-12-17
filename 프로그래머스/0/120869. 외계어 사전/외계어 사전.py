def solution(spell, dic):
    for i in dic:
        if set(spell)==set(i):
            return 1
            break
    return 2