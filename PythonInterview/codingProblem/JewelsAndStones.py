#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:51:43 2020

@author: jihye
"""

# J는 보석이며, S는 갖고 있는 돌이다. S에는 보석이 몇 개나 있을까? 대소문자 구분 
# input : J ="aA" , S = "aAAbbb"
# output : 3



# 해시 테이블 

def newJewelsInStones(J : str, S: str) -> int:
    freqs = {} # 해시 테이블 선언
    count = 0
    
    # 돌 S 의 빈도 수 계산 
    for char in S :
        if char not in freqs :
            freqs[char] = 1
        else:
            freqs[char]+=1
            
    # 보석 J의 빈도 수 계산 
    for char in J :
        if char in freqs:
            count += freqs[char]
            
    return count


# defaultdict 
def newJewelsInStones2( J : str, S : str) -> int:
    import collections
    
    freqs = collections.defaultdict(int)
    count = 0 
    
    # 비교 없이 빈도 계산 
    for char in S :
        freqs[char]+=1
        
    for char in J:
        count += freqs[char]
        
    return count 


# Counter 객체 
def newJewelsInStones3(J : str, S : str) -> int:
    import collections 
    
    freqs = collections.Counter(S)
    count = 0 
    for char in J:
        count += freqs[char]
        
    return count


# 파이썬 방식 
def newJewelsInStones4(J : str, S:str) -> int:
    return sum( s in J for s in S)


J = "aA"
S = "aAAbbb"

print(newJewelsInStones4(J, S))

    

    





