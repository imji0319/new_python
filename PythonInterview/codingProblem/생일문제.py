#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 19:39:37 2020

@author: jihye

생일의 가짓수는 365개로 여러 사람이 모였을때 생일이 같은 2명이 존재할 확률은 366명 이상 모여야 일어나는 일 같다.
하지만 실제로는 23명만 모여도 50%가 넘고, 57명이 모이면 그때부터는 99%가 넘어간다. 



"""

import random

TRIALS = 100000 # 10만번 실험 
same_BD = 0 # 생일이 같은 실험의 수 


# 10만번의 실험 실행 

for _ in range(TRIALS):
    birthdays = []
    
    # 23명이 모얐을 때, 생일이 같을 경우 same_BD += 1
    for i in range(57):
        birthday = random.randint(1, 365)
        
        if birthday in birthdays:
            same_BD +=1
            break
        
        birthdays.append(birthday)
        
# 전체 10만 번 실험 중 생일 같은 실험의 확률 
print(f'{same_BD/TRIALS * 100}%')
    
