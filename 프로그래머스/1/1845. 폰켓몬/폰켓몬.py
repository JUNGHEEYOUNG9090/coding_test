def solution(nums):
    
    s = set()
    
    for i in range(0,len(nums)) :
        if len(s) == len(nums)/2:
            break
        else :
            s.add(nums[i])
    
    answer = len(s)
    
    return answer