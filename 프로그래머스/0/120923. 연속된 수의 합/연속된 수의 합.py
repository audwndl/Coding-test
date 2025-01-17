def solution(num, total):
    if num == 1:
        return [total]
    
    # 연속된 수의 시작점 계산
    a = (total - (num * (num - 1)) // 2) // num
    
    # 연속된 수 리스트 생성
    return [a + i for i in range(num)]
