'''
Created on 2020. 9. 2.

@author: jihye
'''

T = int(input()) # T개의 테스트 케이스 

result = []
for i in range(T):
    
    x_point=[]
    y_point=[]
    
    for j in range(3):
        
        test_case = input().split()
        x_point.append(test_case[0])
        y_point.append(test_case[-1])

    x = x_point[0]
    y = y_point[0]
    
    for n in x_point:
        if x_point.count(n) != 2:
            x = n
    
    for m in y_point:
        if y_point.count(m) != 2 :
            y = m

    result.append(x+" "+y)

for i in result:
    print(i)
    