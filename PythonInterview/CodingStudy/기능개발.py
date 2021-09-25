import math
def solution(progresses, speeds):
    answer = []
    release_days = []
    
    for i in range(len(progresses)):
        release_days.append(math.ceil((100 - progresses[i])/speeds[i]))
    
    days = release_days[0]
    n = 1 
    #print(release_days)
    for i in range(1,len(release_days)):
        if days >= release_days[i] : 
            n+=1
        else:
            answer.append(n)
            days = release_days[i] 
            n=1 
            
        if i == len(release_days) - 1:
            answer.append(n)
        
        #print(i, days , n, answer)
            
            
        
            
        
    return answer
