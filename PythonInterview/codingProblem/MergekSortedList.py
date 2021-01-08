#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 19:24:44 2020

@author: jihye
"""

# K개의 정렬된 리스트를 1개의 정렬된 리스트로 병합 

from typing import List, ListNode
import headq # 우선순위 큐 문제에 자주 사용 됨 

def mergeKLists(lists : List[ListNode]) -> ListNode : 
    
    root = result = ListNode(None)
    heap = []
    
    # 각 연결 리스트의 루트를 입에 저장 
    for i in range(len(lists)):
        if lists[i] : 
            headq.heappush(heap, (lists[i].val, i, lists[i]))
            
    # 힙 추출 이후 다음 노드는 다시 저장 
    while heap : 
        node = headq.heappop(heap) # heappop() : r가장 작은 노드의 연결리스트부터 차례로 추출 
        idx = node[1]
        result.next =node[2]
        
        result = result.next 
        if result.next :
            headq.heappush(heap, (result.next.val, idx, result.next))
            
    return root.next
