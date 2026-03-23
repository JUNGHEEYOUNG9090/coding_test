def solution(arr):
    if not arr:
        return []

    answer = [arr[0]]  

    for num in arr[1:]:
        if num != answer[-1]:  
            answer.append(num)

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    return answer