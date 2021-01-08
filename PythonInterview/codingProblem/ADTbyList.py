#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 16:05:10 2020

@author: jihye
"""

# 연결 리스트를 이용한 스택 ADT 구현

class Node:
    def __init__(self, item, next ):
        self.item = item
        self.next = next 
        
        
class Stack:
    def __init__(self):
        self.last = None
    
    def push(self, item):
        self.last = Node(item, self.last)
    
    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item 


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)


for _ in range(5):
    print(stack.pop())
    
    

    