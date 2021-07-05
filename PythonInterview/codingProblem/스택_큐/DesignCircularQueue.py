#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 17:42:56 2020

@author: jihye
"""

# Q. 원형 큐를 디자인 하라

# FIFO 구조를 지닌다는 점에서 기존의 큐와 비슷하지만 마지막 위치가 시작 위치와 연결되는 원형 구조 

class MyCircularQueue :
    def __init__(self, k : int ):
        self.q = [None]*k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0
        
    
    # enQueue() : rear 포인트 이동 
    def enQueue(self, value : int ) -> bool :
        if self.q[self.p2] is None : 
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1 ) % self.maxlen
            
            return True
        return False
    
    #deQueue() : front 포인터 이동 
    def deQueue(self) -> bool:
        if self.q[self.p1] is None :
            return False
        else: 
            self.q[self.p1]=None
            self.p1 = (self.p1 + 1)%self.maxlen
            return True
        
        
    def Front(self) -> int:
        return -1 if self.q[self.p1] is None else self.q[self.p1]
    
    def Rear(self) -> int :
        return -1 if self.q[self.p2-1] is None else self.q[self.p2-1]
    
    
    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None 
    
    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None
    
    

    
    
    
    