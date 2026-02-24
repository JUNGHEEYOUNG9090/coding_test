import datetime

def solution(a, b):
    
    date = datetime.datetime(2016,a,b)
    dt = date.weekday()
    
    
    if dt == 0 :
        answer = 'MON'
    if dt == 1 :
        answer = 'TUE'
    if dt == 2:
        answer = 'WED'
    if dt == 3:
        answer = 'THU'
    if dt == 4:
        answer = 'FRI'
    if dt == 5:
        answer = 'SAT'
    if dt == 6:
        answer = 'SUN'
    


    
    return answer
    