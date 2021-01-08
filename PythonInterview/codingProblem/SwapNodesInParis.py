'''
Created on 2020. 10. 15.

@author: jihye
'''

'''
페어(pair)단위로 스왑하라.
'''




class ListNode():
    
    def __init__(self, x):
        self.val = x 
        self.next = None


# 값만 교환 
def swapPairs(head : ListNode) -> ListNode :
    
    cur = head 
    
    while cur and cur.next :
        
        # 값만 교환 
        
        cur.val , cur.next.val = cur.next.val, cur.val
        
        cur = cur.next.next
        
    
    return head 

# 반복 구조로 스왑 

def swapPairs2(head : ListNode) -> ListNode:
    
    root = prev = ListNode(None)
    
    prev.next = head 
    
    while head and head.next : 
        # b 가 a(head)를 가리키도록 할당 
        
        b = head.next 
        head.next = b.next 
        b.next = head 
        
        # prev 가 b를 가리키도록 할당 
        prev.next = b 
        
        #다음번 비교를 위해 이동 
        head = head.next 
        prev = prev.next.next 
         
    
    return root.next 
        

# 재귀 구조로 변환 
def swapPairs3(head : ListNode ) -> ListNode:
    
    if head and head.next : 
        p = head.next 
        
        # 스왑된 값 리턴 받음 
        head.next = swapPairs3(p.next)
        p.next = head
        return p
    
    return head 


def main():
    
    "1->2->3->4 => (2->1)->(4->3)"
    l_1 = ListNode(1)
    l_2 = ListNode(2)
    l_3 = ListNode(3)
    l_4 = ListNode(4)
    
    l_1.next = l_2
    l_2.next = l_3
    l_3.next = l_4
    #result = swapPairs(l_1)
    #result = swapPairs2(l_1)
    result = swapPairs3(l_1)
    
    # Print elements in ListNode
    string = ""
    while result :
        string += str(result.val)
        if result.next: 
            string +="->"
        result = result.next
    print(string)



if __name__ == "__main__":
    
    main()
