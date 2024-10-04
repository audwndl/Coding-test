def solution(rank, attendance):
    attend_list = [(i,j) for i,j in list(enumerate(rank)) if attendance[i]]
        
    # 등수 기준으로 오름차순 정렬
    attend_list.sort(key=lambda x: x[1])
    
    a, b, c = attend_list[0][0], attend_list[1][0], attend_list[2][0]
    return 10000 * a + 100 * b + c
