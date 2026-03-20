import math
def solution(s):
    
    n = len(s)//2
    
    if len(s) % 2 == 1 :
        answer = s[n]
    else :
        answer = s[n-1] + s[n] 
    return answer