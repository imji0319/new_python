#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 18:51:10 2020

@author: jihye
"""

from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyCircularDeque:
    
    # 초기화 : 오왼 인덱스 정의 : head/tail, 최대 길이 정보 : k, 길이정보 : len
    def __init__(self, k : int):
        
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k , self.len = k , 0
        self.head.right , self.tail.left = self.tail, self.head 
        
    
    # 이중 연결 리스트에 신규 노드 삽입 
    def _add(self, node : ListNode, new : ListNode ):
        n = node.right
        node.right = new 
        new.left, new.right = node, n 
        n.left = new 
        
        
    def _del(self, node : ListNode) :
        n = node.right.right 
        node.right = n 
        n.left = node 
    
    # 데크 처음에 아이템을 추가하고 성공할 경우 true 리턴  

    def insertFront(self, value : int) -> bool:
        if self.len == self.k : 
            return False
        
        self.len+= 1
        self._add(self.head, ListNode(value))
        return True 
        

    # 데크 마지막에 아이템을 추가하고 성공할 경우 true 리턴 
    def insertLast(self, value : int) -> bool:
        if self.len == self.k:
            return False 
        
        self.len+=1
        self._add(self.tail, ListNode(value))
        return True
    
    # 데크 처음에 아이템을 삭제하고 성공할 경우 true 
    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        
        self.len -= 1
        self._del(self.head)
        return True

    
    # 데크 마지막에 아이템을 삭제하고 성공할 경우 true 
    def deleteLast(self) -> bool:
        if self.len == 0:
            return False 
        
        self.len -= 1
        self._del(self.tail.left.left)
        return True
        
    # 데크첫번째 아이템을 가져오고, 비어 있으면 -1 
    def getFront(self) -> int :
        return self.head.right.val if self.len else -1 
    
    # 데크 마지막 아이템을 가져오고, 비어있으면 -1
    def getLast(self) -> int:
        return self.tail.left.val if self.len else -1 
    
    # 비어 있는지 여부 
    def isEmpty(self) -> bool:
        return self.len == 0
    
    # 데크가 가득 차있는지 여부 
    def isFull(self) -> bool :
        return self.len == self.k
    

    
    
        
    
    # 데크 마지막 아이템을 가져오고, 비어있으면 -1
        
    
        
        
        
        
        
    


