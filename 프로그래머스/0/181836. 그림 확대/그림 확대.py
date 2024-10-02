def solution(picture, k):
    result = []
    
    # 각 줄의 각 문자를 k번 반복한 새로운 줄을 만든 후 k번 추가
    for row in picture:
        expanded_row = ''.join([char * k for char in row])  # 각 문자를 k번 반복
        for _ in range(k):
            result.append(expanded_row)  # k번 반복하여 세로로 확장
    
    return result
