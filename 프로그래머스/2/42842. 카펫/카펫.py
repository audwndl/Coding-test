def solution(brown, yellow):
    yaksu = [] 
    # 노란색 칸의 개수는 노란사각형의 넓이, 
    # 가로*세로 = 넓이 이기때문에 넓이의 약수를 구한다.
    for i in range(1,yellow+1):
        if yellow%i==0:
            yaksu.append(i)
    
    for i in yaksu:
        for j in yaksu:
            if (i+j)*2+4==brown and i*j==yellow: 
            # 감싼 테두리의 길이가 brown과 같고, 넓이가 yellow와 같으면
                return sorted([i+2,j+2],reverse=True) #가로세로 정렬