'''
Created on 2020. 9. 27.

@author: jihye
'''

from typing import List

'''
문자열을 뒤집는 함수

input : string list 

BUT, modify list without Return
'''


def reverseString(s : List[str]) -> None: # List : from typing 
    left, right = 0, len(s) -1 
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left +=1
        right -=1
    
def reverseString2(s : List[str]) :
    s.reverse()
    
    
def reverseString3(s : List[str]) :
    s[:] = s[::-1]  # 뒤집어 저장 


def main():
    s = ['h','e','l','l','o']
    reverseString(s)
    reverseString2(s)
    

if __name__ == '__main__':
    main()