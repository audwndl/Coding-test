def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
    
    if len(answer)>=k:
        answer = answer[:k]
    else :
        for i in range(k-len(answer)):
            answer.append(-1)
    return answer