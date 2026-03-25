def solution(n):
    answer = []
    
    lst =  list(str(n))
    for num in range(len(lst)-1,-1,-1):
        answer.append(int(lst[num]))

    return answer