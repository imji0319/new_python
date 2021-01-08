#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 17:34:37 2020

@author: jihye
"""

# 스택을 이용해 큐 구현 
# 연산 기능 : push(x), pop(), peek(), empty()


class MyQueue:
    
    def __init__(self):
        self.input = []
        self.output = []
        
    
    def push(self, x):
        self.input.append(x)
        
    def pop(self):
        self.peek()
        return self.output.pop()
    
    def peek(self):
        #output 이 없으면 모두 재입력 
        if not self.output : 
            while self.input:
                self.output.append(self.input.pop())
        
        return self.output[-1]
    
    def empty(self):
        return self.input == [] and self.output == []


queue = MyQueue()

queue.push(1)
queue.push(2)
print(queue.peek())
print(queue.pop())
print(queue.empty())
    




