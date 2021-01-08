#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 20:51:21 2021

@author: jihye

서로 다른 정수를 입력받아 가능한 모든 순열 리턴 
"""


from typing import List

def permute(nums : List[int]) -> List[List[int]]:
    
    results = []
    prev_elements = []
    
    def dfs(elements):
        # 리프 노드 일때 결과 추가 
        if len(elements) == 0:
            results.append(prev_elements[:]) # prev_elements[:] 로 하여 반드시 값을 복사하는 형태로 처리 해야함 
            
        
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)
            
            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()
            
        
    
    dfs(nums)
    
    return results 

# itertools 모듈 사용 

import itertools

def permute2(nums : List[int]) -> List[List[int]]:
    return list(map(list, itertools.permutations(nums)))

# itertools.permutation 의 output은 tuple로 이를 리스트로 변환하여야 함. 