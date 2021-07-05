'''
Created on 2020. 10. 24.

@author: jihye
'''

'''
연결리스트를 홀수 노드 다음에 짝 수 노드가 오도록 재구성하라. 
공간 복잡도 O(1), 시간복잡도 O(n)에 필요하라.
'''


class ListNode():
    
    def __init__(self,x):
        self.val = x 
        self.next = None
        

# 반복 구조로 홀짝 노드 처리 
def oddEvenList(head : ListNode) -> ListNode:
    
    # 예외 처리 
    if head is None :
        return None 
    
    odd = head 
    even = head.next 
    even_head = head.next 
    
    # 반복하면서 홀짝 노드 처리
    while even and even.next : 
        odd.next, even.next = odd.next.next, even.next.next 
        
        odd, even = odd.next, even.next 
        
    # 홀수 노드의 마지막을 짝수 헤드로 연결 
    
    odd.next = even_head 
    
    return head



def main():
    
    l_1 = ListNode(1)
    l_2 = ListNode(2)
    l_3 = ListNode(3)
    l_4 = ListNode(4)
    l_5 = ListNode(5)
    l_6 = ListNode(None)
    
    l_1.next = l_2
    l_2.next = l_3
    l_3.next = l_4
    l_4.next = l_5
    l_5.next = l_6
    
    result = oddEvenList(l_1)
    
    # Print elements in ListNode
    string = ""
    while result :
        string += str(result.val)
        if result.next: 
            string +="->"
        result = result.next
    print(string)


if __name__ == '__main__':
    main()