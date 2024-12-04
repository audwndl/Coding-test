def solution(my_str, n):
    answer = []
    i = 0  # 시작 인덱스
    while i + n <= len(my_str):
        answer.append(my_str[i:i+n])
        i += n
    if i < len(my_str):  # 남은 문자열이 있을 때만 추가
        answer.append(my_str[i:])
    return answer
