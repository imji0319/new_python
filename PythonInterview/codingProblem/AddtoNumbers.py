'''
Created on 2020. 10. 15.

@author: jihye
'''

from typing import List

'''
역순으로 저장된 연결 리스트의 숫자를 더하라. 
'''

class ListNode:
    def __init__(self, x):
        self.val = x 
        self.next = None
        
## 자료형 변환 


# 역순으로 된 연결리스트를 재정렬 
def reverseList(head : ListNode) -> ListNode:
    
    node, prev = head, None
    
    while node:
        next, node.next = node.next, prev
        prev, node = node, next 
        
    return prev


# 연결리스트를 파이썬 리스트로 변경 
def toList(node : ListNode) -> ListNode:
    
    list: List = []
    
    while node :
        list.append(node.val)
        node = node.next 
    
    return list 

# 리스트를 연결리스트로 변경 
def toReversedLinkedList(result : ListNode) -> ListNode :
    
    prev : ListNode = None 
    
    for r in result : 
        node = ListNode(r)
        node.next = prev
        prev = node  
        
    return node


def addTwoNumbers(l1 : ListNode, l2 : ListNode ) -> ListNode :
    
    a = toList(reverseList(l1))
    b = toList(reverseList(l2))
    
    resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b ))
    
    
    return toReversedLinkedList(str(resultStr))
                


def addTwoNumbers2(l1 : ListNode, l2 : ListNode ) -> ListNode: 
    
    root = head = ListNode(0)    
    
    carry = 0
    
    while l1 or l2 or carry :
        sum = 0
        # 두 입력값의 합 계산 
        
        if l1 : 
            sum += l1.val
            l1 = l1.next 
            
        if l2 : 
            sum += l2.val
            l2 = l2.next 
            
        
        # 몫(자리올ㄹ미수)과 나머지(값) 계산
        
        carry, val = divmod(sum + carry, 10 )
        head.next = ListNode(val)
        
        head = head.next
        
    return root.next



if __name__ == '__main__':
    pass