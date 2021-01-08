'''
Created on 2020. 10. 4.

@author: jihye
'''


'''

연결리스트가 펠리드롬 구조인지 판별 

ex)

input : 1->2 output : False
input : 1->2->2->1 output : True 

'''


from typing import List
import collections
from typing import Deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# ListNode 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



def isPalindrome(head : ListNode) -> bool :
    
    q : List = []
    
    if not head : # 비어있는 값인지 확인 
        return True 
    
    node = head
    
    # 리스트 반환 
    while node is not None:
        q.append(node.val)
        node = node.next 
    
    # 팰린드롬 판별 
    while len(q) > 1: 
        if q.pop(0) != q.pop():
            return False
        
    return True


def isPalindrome2(head : ListNode) -> bool: 
    
    q: Deque = collections.deque()
    
    if not head:
        return True
    
    node = head 
    
    while node is not None :
        q.append(node.val)
        node = node.next
        
    while len(q) > 1: 
        if q.popleft() != q.pop():
            return False 
        
    return True


# Runner 기법 
def isPalindrome3(head: ListNode) -> bool:
    
    # 역순 연결 리스트 
    rev = None 
    
    # 빠른러너와 느린 러너의 초깃값은 모두 head에서 출발 
    slow = fast = head     
    
    # 러너 이동 : next가 존재하지 않을 때까지 이동 
    while fast and fast.next : 
        fast = fast.next.next
        
        # 다중 할당 
        rev, rev.next, slow = slow, rev, slow.next 
    
    if fast : # fast 이 아직 None 이 아닌 경우  -> 홀수 일 경우 slow 러너가 한칸 앞으로 이동하여 중앙의 값을 빗겨나가야 함 
        slow = slow.next
        
        
    
    # 팰린드롬 여부 확인 
    
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
        
        
    #return not slow
    return not rev
        
        



def main():
    
    "1->2"
    l_1 = ListNode(1)
    l_2 = ListNode(2)
    l_1.next = l_2

    print(isPalindrome(l_1))
    print(isPalindrome2(l_1))
    
    "1->2->2->1"
    l_1 = ListNode(1)
    l_2 = ListNode(2)
    l_3 = ListNode(2)
    l_4 = ListNode(1)
    
    l_1.next = l_2
    l_2.next = l_3
    l_3.next = l_4
    
    print(isPalindrome(l_1))
    print(isPalindrome2(l_1))
    
    
    "1->2->3->2->1"
    l_1 = ListNode(1)
    l_2 = ListNode(2)
    l_3 = ListNode(3)
    l_4 = ListNode(2)
    l_5 = ListNode(1)
    
    l_1.next = l_2
    l_2.next = l_3
    l_3.next = l_4
    l_4.next = l_5
    
    
    print(isPalindrome(l_1))
    print(isPalindrome2(l_1))
    print(isPalindrome3(l_1))
    

if __name__ == '__main__':
    main()