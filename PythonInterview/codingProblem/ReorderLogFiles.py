'''
Created on 2020. 9. 27.

@author: jihye
'''

from typing import List

'''
로그를 재정렬 하라 

기준 
1. 로그의 가장 앞 부분은 식별자
2. 문자로 구성된 로그가 숫자로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다. 

'''

def ReorderLogFiles(logs : List[str]) -> List[str]:
    
    letters, digits = [], [] 
    
    for log in logs : 
        # print(log.split()[1])
        
        if log.split()[1].isdigit():
            # split()[1] : 식별자 다음으로 로그 시작 부분 , isdigit() : 숫자여부 판단 
            digits.append(log)
            
        else:
            letters.append(log)
            


    # x.split()[1:] : 식별자제외하고 정렬 -> x.split()[0] : 식별자 지정, 동일한 경우 식별자로 정렬 
    letters.sort(key = lambda x : (x.split()[1:], x.split()[0]))
    
    
    return letters+digits
            
    


def main():
    
    logs = ["dig1 8 1 5 1", "let1 art can","dig2 3 6", "let2 own kit dig", "let3 art zero"]
    
    print(ReorderLogFiles(logs))

if __name__ == '__main__':
    main()