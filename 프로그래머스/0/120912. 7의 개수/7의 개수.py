def solution(array):
    combined = "".join(map(str, array))
    return combined.count('7')