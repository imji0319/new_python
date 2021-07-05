'''
Created on 2020. 10. 4.

@author: jihye
'''

'''
연결 리스트를 뒤집어라 .
'''


class ListNode:
    def __init__(self, x):
        self.val = x 
        self.next = None


# 재귀 구조로 뒤집기 

def reverseList(head : ListNode) -> ListNode :
    
    def reverse(node : ListNode, prev : ListNode = None): 
        
        if not node : 
            return prev # node : 현재 노드 
        
        next, node.next = node.next, prev # 백트래킹 -> 거꾸로 연결 
        return reverse(next, node)
    
    return reverse(head)



# 반복 구조로 뒤집기 
def reverseList2(head : ListNode) -> ListNode:
    
    node, prev = head, None
    while node:
        next, node.next = node.next, prev
        prev, node = node, next 
        
    return prev



if __name__ == '__main__':
    "1->2->3->4->5->NULL"
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    #l6 = ListNode(None)
    
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    #l5.next = l6
    
    
    #print(reverseList(l1))
    
    #result = reverseList(l1)
    result = reverseList2(l1)
    
    string =""
    while result :
        string +=str(result.val)
        if result.next:
            string +="->"
        result = result.next
        
    print(string)
    
    
    
    