#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 16:33:25 2020

@author: jihye
"""

# 중복한 문자를 제외하고 사전식 순서 Lexicographical Order 로 나열 input : "bcabc" -> output : "abc"
# 사전식 순서 : 사전에서 가장 먼저 찾을 수 있는 순서 

# 재귀 방법 
def removeDuplicateLetters(s: str) -> str :
    
    # 집합으로 정렬 
    for char in sorted(set(s)):
        suffix = s[s.index(char):] # char 위치 부터 맨 뒤까지 suffix 
        # 전체 집합과 접미사 집합이 일치할 때 분리 진행
        if set(s) == set(suffix):
            return char + removeDuplicateLetters(suffix.replace(char,''))
    
    return ''

s = "bcabc"
s2 = "ecbacdcbc" # e 는 사전적으로 맨 뒤지만 입력값에서 한번만 등장하기 때문에 맨 앞 등장 
print(removeDuplicateLetters(s2))
        

# 스택 
def removeDuplicateLetters2(s :str) -> str :
    import collections
    
    counter, seen, stack = collections.Counter(s), set(), []
    
    for char in s:
        counter[char] -= 1
        
        if char in seen :
            continue 
        
        # 뒤에 붙일 문자가 남아 있다면 스택에서 제거 - stack[-1] : 가장 최근 요소 
        while stack and char < stack[-1] and counter[stack[-1]] > 0 : 
            seen.remove(stack.pop())
            
        stack.append(char)
        seen.add(char)
        
    return ''.join(stack)


print(removeDuplicateLetters2(s2))
        






