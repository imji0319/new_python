def solution(s):
    answer = True
    
    if len(s) not in [4,6]:
        answer = False
    try :
        list(map(int, s))
    except :
        answer = False
    return answer
