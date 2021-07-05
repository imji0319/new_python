#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 17:02:17 2020

@author: jihye
"""

# 매일 의 화씨 온도(F) 리스트 T를 입력받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지 출력 
# input : T =[73,74,75,71,69,72,76,73] -> output : [1,1,4,2,1,1,0,0]

from typing import List 

# 스택 값 비교 

def dailyTempertures(T : List[int]) -> List[int] : 
    answer = [0]*len(T)
    stack = []
    
    for i, cur in enumerate(T):
        # 현재 온도가 스택 값 보다 높다면 answer 처리 
        while stack and cur >T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        
        stack.append(i)
        
    return answer 


        
T =[73,74,75,71,69,72,76,73]

print(dailyTempertures(T))