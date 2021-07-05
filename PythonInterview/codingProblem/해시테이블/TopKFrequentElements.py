#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 18:27:16 2020

@author: jihye
"""

# k번 이상 등장하는 요소 추출 

from typing import List
import collections
import heapq

# Counter 객체 
def topKFrequent(nums : List[int], k =int ) -> List[int] :
    
    freqs = collections.Counter(nums)    
    freqs_heap =[]
    
    
    # 힙에 음수로 저장 
    for f in freqs: 
        heapq.heappush(freqs_heap, (-freqs[f], f))
        
        
    topk = list()
    
    # k 번 만큼 추출, 최소 힙이므로 가장 작은 음수 순으로 추출 
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])
        
    return topk



# 파이썬 다운 방식  
def topKFrequent2( nums : List[int], k = int) -> List[int]:
    return list(zip(*collections.Counter(nums).most_common(k)))[0]


    
    
    
    
    
    