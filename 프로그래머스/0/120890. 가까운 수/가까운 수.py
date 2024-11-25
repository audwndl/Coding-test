def solution(array, n):
    closest = None
    min_diff = 100
    
    for i in array:
        # 현재 숫자와 n 차이
        diff = abs(i - n)
        
        # 차이가 더 작거나, 차이가 같으면 더 작은수로 업데이트
        if diff < min_diff or (diff == min_diff and i < closest):
            min_diff = diff
            closest = i
    
    return closest
