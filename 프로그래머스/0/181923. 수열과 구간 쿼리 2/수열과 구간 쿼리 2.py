def solution(arr, queries):
    result = []
    
    for s, e, k in queries:
        min_arr = max(arr)+1
        for i in range(s, e + 1):
            if arr[i] > k:
                min_arr = min(min_arr, arr[i])
        
        # 조건을 만족하는 값이 없다면 -1을 저장
        if min_arr == max(arr)+1:
            result.append(-1)
        else:
            result.append(min_arr)
    
    return result