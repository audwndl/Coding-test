def solution(n,a,b):
    count=1
    a,b = (a,b) if a<b else (b,a) # a b 정렬
    while not(b-a==1 and a%2==1): # 두수의 차가 1이고, 첫번째 숫자가 홀수여야 만남
        count+=1
        a = (a+1)//2
        b = (b+1)//2
    return count