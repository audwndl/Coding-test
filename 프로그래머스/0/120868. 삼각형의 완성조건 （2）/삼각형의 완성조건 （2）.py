def solution(sides):
    # 두 변 중 짧은 변과 긴 변을 정리
    short, long = sorted(sides)
    
    # 가능한 x의 범위를 계산
    min_x = long - short + 1  # x가 긴 변 - 짧은 변보다 커야 함
    max_x = long + short - 1  # x가 긴 변 + 짧은 변보다 작아야 함
    
    # 가능한 x의 개수 계산
    return max_x - min_x + 1