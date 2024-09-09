def solution(s):
    s = s.lower().split(" ") #일단 모두 소문자로 만들고 공백을 기준으로 나누기
    a = [] #변경된 문자열이 담길 리스트
    for i in s:
        if i: #i가 공백문자가 아니라면
            a.append(i[0].upper()+i[1:]) #i의 0번 인덱스를 대문자로 바꾸고 a에 추가한다
        else: #공백문자라면(연속해서 나올수 있기때문, string index out of range가 뜸)
            a.append(i) #a에 그대로 넣는다
    return " ".join(a) #사이에 띄어쓰기를 하면서 a를 문자열로 합친다