'''
Created on 2020. 10. 4.

@author: jihye
'''


'''
정렬되어 있는 두 연결 리스트를 합쳐라 
'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x 
        self.next = None
    
    
        


def mergeTwoList(l1 : ListNode, l2 : ListNode) -> ListNode:
    if (not l1) or (l2 and (l1.val > l2.val)): # or 보다 and 연산이 빠름 
        l1, l2 = l2, l1
        
    if l1 :
        l1.next = mergeTwoList(l1.next, l2)
        
    return l1




def main ():
    
    "1->2->4"
    l_1 = ListNode(1)
    l_2 = ListNode(2)
    l_3 = ListNode(4)
    
    l_1.next = l_2
    l_2.next = l_3
    
    "1->3->4"
    l2_1 =ListNode(1)
    l2_2 =ListNode(3)
    l2_3 =ListNode(4)
    
    l2_1.next = l2_2
    l2_2.next = l2_3
    
    
    result = mergeTwoList(l_1, l2_1)
    
    
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