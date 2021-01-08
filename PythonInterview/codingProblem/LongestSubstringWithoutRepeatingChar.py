#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 18:14:18 2020

@author: jihye
"""

# 중복 문자 없는 가장 긴 문자열 의 길이 

def lengthOfLongestSubstring(s : str ) -> int: 
    used = {} # 출현 문자 저장 해시 테이블 
    
    max_length = start = 0 
    
    for index, char in enumerate(s):
        # 이미 등장한 문자는 start 위치 갱신, 전에 등장 여부 무시 <= used[char]
        if char in used and start <=used[char]: 
            start = used[char] + 1
            
        else : # 최대 부분 문자열 길이 갱신 
        
            max_length = max(max_length, index - start + 1)
            
        
        # 현재 문자의 위치 삽입 
        used[char] = index 
        
    return max_length


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwekew"))            







