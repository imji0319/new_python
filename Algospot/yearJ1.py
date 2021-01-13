#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 20:06:38 2021

@author: jihye
"""

year = int(input("연도를 입력하시오 : "))

# 윤년은 4년마다 돌아오며 100년마다 평년으로 돌아간다. 
# 그리고 400년마다 윤년 
# => 4의 배수는 윤년이나 100의 배수는 평년 , 하지만 400의 배수는 윤년 


yearsum = 0 

for i in range(1, year):
    if i%4 == 0 :
        if i%400 == 0: 
            yearsum+=366
            
        elif i%100 == 0:
            yearsum+=365
            
        else :
            yearsum+=366
       
    else :
        yearsum+=365 

weeks = ["월","화","수","목","금","토","일"]     

res = yearsum%7   
result = weeks[res]
        
print(yearsum, result)