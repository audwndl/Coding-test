def solution(my_string):
    arr = []
    for i in my_string :
        if not arr:
            arr.append(i)
        else:
            if i not in arr :
                arr.append(i)
    return "".join(arr)