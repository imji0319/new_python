'''
Created on 2020. 10. 24.

@author: jihye
'''

'''
인덱스 m부터 n까지를 역순으로 만들어라.
'''

class ListNode():
    
    def __init__(self, x):
        self.val = x 
        self.next = None
        


def reverseBetween(head : ListNode, m : int , n: int ) -> ListNode:
    
    # 예외 처리
    if not head or m == n:
        return None
    
    
    
    root = start = ListNode(None)
    
    root.next = head 
    
    # start, end 지정 
    for _ in range(m-1):
        
        start = start.next 
    end = start.next 
    
    # 반복하면서 노드 차례로 뒤집기
    for _ in range(n-m):
        
        tmp, start.next, end.next = start.next, end.next, end.next.next 
        start.next.next = tmp
        
        
    return root.next 
        
    


def main():
    
    l_1 = ListNode(1)
    l_2 = ListNode(2)
    l_3 = ListNode(3)
    l_4 = ListNode(4)
    l_5 = ListNode(5)
    l_6 = ListNode(6)
    
    l_1.next = l_2
    l_2.next = l_3
    l_3.next = l_4
    l_4.next = l_5
    l_5.next = l_6
    
    m , n = 2, 5
    
    result = reverseBetween(l_1, m, n)
    
    string =""
    
    while result : 
        string += str(result.val)
        
        if result.next : 
            string +="->"
            
        result = result.next 
        
    print(string)



if __name__ == '__main__':
    main()