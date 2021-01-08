#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 16:19:36 2020

@author: jihye
"""

# Q. 괄호로 된 입력값이 올바른지 판별하라 . input : ()[]{} -> output : True 

def isVaild(s: str ) -> bool:

    stack = [] 
    table = {
    ')' : '(',
    '}' : '{',
    ']' : '['
    }
   
    
    # 스택 이용 예외 처리 및 일치 여부 판별 
    for char in s:
        if char not in table:
            stack.append(char)
            
        elif not stack or table[char] != stack.pop() : 
            return False
    return len(stack)==0


string = '(){}[]'

print(isVaild(string))

